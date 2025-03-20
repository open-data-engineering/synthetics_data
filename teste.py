from generator.core import SyntheticDataGenerator
from helpers.bigquery_helper import BigQueryHelper

PROJECT_ID = "yams-lab-nonprod"
DATASET_ID = "raw"

generator = SyntheticDataGenerator()
data = generator.generate()

table_name = "users"
records = data["users"]

bq_helper = BigQueryHelper(PROJECT_ID, DATASET_ID, table_name)

bq_helper.write_data(records)
