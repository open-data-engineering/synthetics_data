from datetime import datetime
from generator.core import SyntheticDataGenerator
from helpers.bigquery_helper import BigQueryHelper

PROJECT_ID = "yams-lab-nonprod"
DATASET_ID = "raw"

TABLE_SCHEMAS = {
    "users": [
        {"name": "user_id", "type": "STRING"},
        {"name": "name", "type": "STRING"},
        {"name": "email", "type": "STRING"},
        {"name": "phone", "type": "STRING"},
        {"name": "created_at", "type": "TIMESTAMP"},
    ],
    "accounts": [
        {"name": "account_id", "type": "STRING"},
        {"name": "account_type", "type": "STRING"},
        {"name": "balance", "type": "INTEGER"},
        {"name": "currency", "type": "STRING"},
        {"name": "status", "type": "STRING"},
        {"name": "user_id", "type": "STRING"},
        {"name": "created_at", "type": "TIMESTAMP"},
    ],
    "transactions": [
        {"name": "transaction_id", "type": "STRING"},
        {"name": "amount", "type": "FLOAT"},
        {"name": "currency", "type": "STRING"},
        {"name": "timestamp", "type": "TIMESTAMP"},
        {"name": "account_id", "type": "STRING"},
    ],
}

generator = SyntheticDataGenerator()
data = generator.generate()

for table_name, records in data.items():
    if table_name not in TABLE_SCHEMAS:
        print(f"⚠️ Esquema para a tabela '{table_name}' não definido. Pulando...")
        continue

    formatted_records = []
    for record in records:
        if hasattr(record, "to_dict"):
            record_dict = record.to_dict()
        else:
            record_dict = record.__dict__
        
        for key, value in record_dict.items():
            if isinstance(value, datetime):
                record_dict[key] = value.isoformat()
        
        formatted_records.append(record_dict)

    bq_helper = BigQueryHelper(PROJECT_ID, DATASET_ID, table_name)

    bq_helper.write_data(formatted_records)
