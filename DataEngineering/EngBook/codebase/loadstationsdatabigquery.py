from google.cloud import bigquery 

PROJECT_ID = "dataengpart1"
# where the json file is located 
GCS_URI = "gs://eng-data-bucket/mysql_export/stations/20180102/stations.csv".format(PROJECT_ID) 
# Set the TABLE_ID variable to the ID of the BigQuery table to which the data will be loaded. 
TABLE_ID = "{}.raw_bikesharing.stations".format(PROJECT_ID) 

def load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, table_schema):
    client = bigquery.Client() 
    job_config = bigquery.LoadJobConfig(
        schema = table_schema, 
        source_format = bigquery.SourceFormat.CSV, 
        write_disposition = 'WRITE_TRUNCATE', 
    )
    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config 
    )
    load_job.result() 
    table = client.get_table(TABLE_ID) 

    print("Loaded {} rows to table{}".format(table.num_rows, TABLE_ID)) 

bigquery_table_schema = [
        bigquery.SchemaField("station_id", "STRING"), 
        bigquery.SchemaField("name", "STRING"), 
        bigquery.SchemaField("region_id", "STRING"), 
        bigquery.SchemaField("capacity", "INTEGER")
    ]

if __name__ == "__main__":
    load_gcs_to_bigquery_snapshot_data(GCS_URI, TABLE_ID, bigquery_table_schema)