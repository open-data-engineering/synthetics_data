from google.cloud import bigquery
from datetime import datetime
from typing import List, Dict


class BigQueryHelper:
    def __init__(self, project_id: str, dataset_id: str, table_id: str):
        """Inicializa o cliente do BigQuery."""
        self.client = bigquery.Client(project=project_id)
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.table_ref = f"{project_id}.{dataset_id}.{table_id}"

    def create_table_if_not_exists(self, schema: List[Dict[str, str]]):
        """Cria a tabela no BigQuery se ela não existir."""
        dataset_ref = self.client.dataset(self.dataset_id)
        table_ref = dataset_ref.table(self.table_id)

        try:
            self.client.get_table(table_ref)
            print(f"✅ Tabela {self.table_ref} já existe.")
        except Exception:
            table_schema = [
                bigquery.SchemaField(field["name"], field["type"]) for field in schema
            ]

            table = bigquery.Table(table_ref, schema=table_schema)
            self.client.create_table(table)
            print(f"✅ Tabela {self.table_ref} criada com sucesso!")

    def write_data(self, records: List):
        """Insere dados na tabela do BigQuery, garantindo que objetos sejam convertidos corretamente."""
        if not records:
            print("⚠️ Nenhum dado para inserir.")
            return

        formatted_records = []
        for record in records:
            if hasattr(record, "to_dict"):
                record = record.to_dict()

            formatted_record = {
                key: value.isoformat() if isinstance(value, datetime) else value
                for key, value in record.items()
            }
            formatted_records.append(formatted_record)

        if errors := self.client.insert_rows_json(self.table_ref, formatted_records):
            print(f"❌ Erros ao inserir dados: {errors}")
        else:
            print(
                f"✅ Inseridos {len(formatted_records)} registros na tabela {self.table_ref}."
            )
