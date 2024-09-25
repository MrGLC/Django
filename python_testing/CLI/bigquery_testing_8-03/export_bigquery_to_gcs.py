import os
from google.cloud import bigquery
from unittest.mock import Mock

# Mocking setup
class MockBigQueryClient:
    def __init__(self, project=None):
        self.project = project

    def dataset(self, dataset_id):
        return Mock()

    def extract_table(self, table_ref, destination_uri, location='US'):
        print(f"Mock extract table to {destination_uri} from table_ref {table_ref} in location {location}")
        return Mock(job_id="mock_job_id", location=location)

def get_client(project_id):
    if os.getenv('MOCK_BIGQUERY') == '1':
        return MockBigQueryClient(project=project_id)
    else:
        return bigquery.Client(project=project_id)

def export_table_to_gcs(project_id, dataset_name, table_name, bucket_name, file_name):
    client = get_client(project_id)
    
    destination_uri = f"gs://{bucket_name}/{file_name}"
    dataset_ref = bigquery.DatasetReference(project_id, dataset_name)
    table_ref = dataset_ref.table(table_name)
    
    extract_job = client.extract_table(
        table_ref,
        destination_uri,
        # Location must match that of the source table.
        location="US"
    )  
    extract_job.result()  # Waits for the job to complete if not mocked.
    
    print(f"Exported {project_id}:{dataset_name}.{table_name} to {destination_uri}")

# Example usage
if __name__ == '__main__':
    export_table_to_gcs(
        "YOUR_PROJECT_ID",
        "YOUR_DATASET_NAME",
        "YOUR_TABLE_NAME",
        "YOUR_BUCKET_NAME",
        "YOUR_FILE_NAME.csv"  # Specify the format you need (e.g., CSV, JSON)
    )

