from google.cloud import bigquery
import logging

logging.basicConfig(level=logging.INFO)

# Set the PROJECT_ID variable to the ID of the project that contains the target dataset.
PROJECT_ID = "dataengpart1"
# bikeshare regions table 
# Set the PUBLIC_TABLE_ID variable to the ID of the table in the public dataset that contains t
# the data to be loaded, and set the TARGET_TABLE_ID variable to the ID of the 
# target table in the user's dataset. 
PUBLIC_TABLE_ID = "bigquery-public-data.san_francisco_bikeshare.bikeshare_regions"
TARGET_TABLE_ID = f"{PROJECT_ID}.raw_bikesharing.regions"


# load_data_from_bigquery_public() function that takes two parameters: the PUBLIC_TABLE_ID 
# variable that specifies the ID of the source table in the public dataset, and the TARGET_TABLE_ID 
# variable that specifies the ID of the target table in the user's dataset
def load_data_from_bigquery_public(PUBLIC_TABLE_ID, TARGET_TABLE_ID):
    # Create a BigQuery client object using default project credentials.
    client = bigquery.Client() 

    # QueryJobConfig object that specifies the job configuration for the query. The destination parameter 
    # is set to the TARGET_TABLE_ID variable that specifies the ID of the target table. 
    # The write_disposition parameter is set to WRITE_TRUNCATE to overwrite any existing 
    # rows in the target table
    job_config = bigquery.QueryJobConfig(
        destination=TARGET_TABLE_ID, 
        write_disposition="WRITE_TRUNCATE")
    
    # query job that selects all columns from the specified source table. The sql variable is set to a 
    # string that specifies the SQL query to execute. The PUBLIC_TABLE_ID parameter is used to 
    # specify the source table.
    # The job_config parameter is set to the job_config object that specifies the job configuration.
    sql = "SELECT * FROM `{}`;".format(PUBLIC_TABLE_ID)
    try:
        query_job = client.query(sql, job_config=job_config)
        query_job.result()
        logging.info(f"Data loaded from {PUBLIC_TABLE_ID} to {TARGET_TABLE_ID}")
    except Exception as exception: 
        logging.error(f"Error loading data from {PUBLIC_TABLE_ID} to {TARGET_TABLE_ID}: {exception}")

# Call the load_data_from_bigquery_public() function with the PUBLIC
