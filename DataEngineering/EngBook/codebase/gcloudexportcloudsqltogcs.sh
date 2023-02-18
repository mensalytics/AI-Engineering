gcloud sql export csv mysql-instance-source \
gs://eng-data-bucket/mysql_export/stations/20180101/stations.csv \
--database=apps_db \
--offload \
--query='SELECT * FROM stations WHERE station_id <= 200;'

gcloud sql export csv mysql-instance-source \
gs://eng-data-bucket/mysql_export/stations/20180102/stations.csv \
--database=apps_db \
--offload \
--query='SELECT * FROM stations WHERE station_id > 400;'