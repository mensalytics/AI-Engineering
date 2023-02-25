from google.cloud import bigquery

client = bigquery.Client()

TABLE_SCHEMA = [
    bigquery.SchemaField("trip_id", "STRING"),
    bigquery.SchemaField("duration_sec", "INTEGER"),
    bigquery.SchemaField("start_date", "TIMESTAMP"),
    bigquery.SchemaField("start_station_name", "STRING"),
    bigquery.SchemaField("start_station_id", "STRING"),
    bigquery.SchemaField("end_date", "TIMESTAMP"),
    bigquery.SchemaField("end_station_name", "STRING"),
    bigquery.SchemaField("end_station_id", "STRING"),
    bigquery.SchemaField("member_gender", "STRING"),
]

def load_gcs_to_bigquery_event_data(gcs_uri, table_id, table_schema):
    """Load data from a Google Cloud Storage URI to a BigQuery table.

    Args:
        gcs_uri (str): The URI of the source data in Google Cloud Storage.
        table_id (str): The ID of the target table in BigQuery.
        table_schema (List[bigquery.SchemaField]): The schema of the target table.
    """
    if not gcs_uri:
        raise ValueError("The Google Cloud Storage URI must be provided.")
    if not table_id:
        raise ValueError("The BigQuery table ID must be provided.")
    if not table_schema:
        raise ValueError("The BigQuery table schema must be provided.")

    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    )

    load_job = client.load_table_from_uri(gcs_uri, table_id, job_config=job_config)

    load_job.result()

    table = client.get_table(table_id)

    print(f"Loaded {table.num_rows} rows to table {table_id}.")


if __name__ == "__main__":
    project_id = "dataengpart1"
    gcs_uri = f"gs://eng-data-bucket/trips/20180101Data/*.json"
    table_id = f"{project_id}.raw_bikesharing.trips"
    load_gcs_to_bigquery_event_data(gcs_uri, table_id, TABLE_SCHEMA)
