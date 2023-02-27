import sys
import logging
from google.cloud import bigquery 

project_id = "dataengpart1"
target_table_id = "{}.dwh_bikesharing.fact_trips_daily".format(project_id)

logging.basicConfig(level=logging.INFO)

def create_fact_table(project_id, target_table_id): 
    if len(sys.argv) < 2:
        logging.error("Please provide the load date as a command-line argument")
        sys.exit(1)

    load_date = sys.argv[1] 
    logging.info("Load date: %s", load_date) 

    client = bigquery.Client() 
    job_config = bigquery.QueryJobConfig(
        destination=target_table_id, 
        write_disposition='WRITE_APPEND'
    )

    sql = """
        SELECT DATE(start_date) AS trip_date,
            start_station_id,
            COUNT(trip_id) AS total_trips,
            SUM(duration_sec) AS sum_duration_sec,
            AVG(duration_sec) AS avg_duration_sec
        FROM `{project_id}.raw_bikesharing.trips` AS trips
        JOIN `{load_date}.raw_bikesharing.stations` AS stations
            ON trips.start_station_id = stations.station_id
        WHERE DATE(start_date) = @load_date
        GROUP BY trip_date, start_station_id
    """

    job_params = {"load_date": load_date}
    query_job = client.query(sql, job_config=job_config)

    try: 
        query_job.result() 
        logging.info("Query success") 
    except Exception as exception: 
        logging.exception(exception) 

if __name__ == "__main__": 
    create_fact_table(project_id, target_table_id)
