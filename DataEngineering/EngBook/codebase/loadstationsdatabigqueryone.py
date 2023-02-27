# IMPROVEMENT ON THE PREVIOUS VERSION 
# loadstationsdatabigquery.py


from google.cloud import bigquery 


def load_gcs_to_bigquery_snapshot_data(gcs_uri, table_id, table_schema):
    """
    Loads data from a CSV file in Google Cloud Storage to a BigQuery table.

    Args:
        gcs_uri (str): The URI of the CSV file in Google Cloud Storage.
        table_id (str): The ID of the BigQuery table to which the data will be loaded.
        table_schema (list): A list of BigQuery SchemaField objects defining the table schema.
    """
    try:
        client = bigquery.Client()
        job_config = bigquery.LoadJobConfig(
            schema=table_schema,
            source_format=bigquery.SourceFormat.CSV,
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )
        load_job = client.load_table_from_uri(
            gcs_uri, table_id, job_config=job_config
        )
        load_job.result()
        table = client.get_table(table_id)

        print(f"Loaded {table.num_rows} rows to table {table_id}")
    except Exception as e:
        print(f"Error loading data to BigQuery: {e}")

if __name__ == "__main__":
    # Set the project ID, GCS URI, table ID, and table schema
    project_id = "dataengpart1"
    gcs_uri = "gs://eng-data-bucket/mysql_export/stations/20180102/stations.csv"
    table_id = f"{project_id}.raw_bikesharing.stations"
    table_schema = [
        bigquery.SchemaField("station_id", "STRING"),
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("region_id", "STRING"),
        bigquery.SchemaField("capacity", "INTEGER")
    ]
    # Call the function to load the data to BigQuery
    load_gcs_to_bigquery_snapshot_data(gcs_uri, table_id, table_schema)



