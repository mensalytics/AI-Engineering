from google.cloud import bigquery 

PROJECT_ID = "dataengpart1"
# where the json file is located 
GCS_URI = "gs://eng-data-bucket/trips/20180102Data/*.json".format(PROJECT_ID) 
# Set the TABLE_ID variable to the ID of the BigQuery table to which the data will be loaded. 
TABLE_ID = "{}.raw_bikesharing.trips".format(PROJECT_ID) 

client = bigquery.Client() 

# takes three parameters 
# location of the data in GCS 
# ID of the target table in bigquery 
# specifies the schema of the target table 
def load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, table_schema): 
    # Create a LoadJobConfig object that specifies the job configuration for loading the data to BigQuery.
    job_config = bigquery.LoadJobConfig(
        # The schema parameter is set to the table_schema variable that specifies the schema of the target table.
        schema = table_schema, 
        # The source_format parameter is set to NEWLINE_DELIMITED_JSON because the source data is in JSON format.
        source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON, 
        # The write_disposition parameter is set to WRITE_APPEND to append the data to the existing rows in the target table.
        write_disposition = "WRITE_APPEND"
    )

    # Load the data from the specified Google Cloud Storage URI to the specified BigQuery table 
    # using the load_table_from_uri() method of the BigQuery client object. 
    # The job_config parameter is set to the job_config object that specifies the job configuration.
    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config 
    )
    
    # Wait for the load job to complete and return the result.
    load_job.result() 
    # Get a reference to the target table using the get_table() method of the BigQuery client object. 
    # The TABLE_ID parameter specifies the ID of the target table.
    table = client.get_table(TABLE_ID) 
    # Print the number of rows loaded to the target table.
    print("Loaded {} rows to table {}".format(table.num_rows, TABLE_ID))

# Schema of the table being loaded into bigquery 
bigquery_table_schema = [
    bigquery.SchemaField("trip_id", "STRING"),
    bigquery.SchemaField("duration_sec", "INTEGER"),
    bigquery.SchemaField("start_date", "TIMESTAMP"),
    bigquery.SchemaField("start_station_name", "STRING"),
    bigquery.SchemaField("start_station_id", "STRING"),
    bigquery.SchemaField("end_date", "TIMESTAMP"),
    bigquery.SchemaField("end_station_name", "STRING"),
    bigquery.SchemaField("end_station_id", "STRING"),
    bigquery.SchemaField("member_gender", "STRING")
]
if __name__ == "__main__":
    load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, bigquery_table_schema)