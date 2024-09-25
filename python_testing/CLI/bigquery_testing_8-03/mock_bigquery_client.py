from unittest.mock import Mock

# Mock the BigQuery client
MockBigQueryClient = Mock()
MockBigQueryClient.extract_table.return_value.result.return_value = True

def get_client(mock=False):
    if mock:
        return MockBigQueryClient
    else:
        from google.cloud import bigquery
        return bigquery.Client()

