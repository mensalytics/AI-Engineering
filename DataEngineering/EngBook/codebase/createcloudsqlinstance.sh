# DIFFERENT WATS TO CREATE CLOUD SQL INSTANCE 
# USING UI, GCLOUD, TERRAFORM, RESTv1, Restv1beta4 
# YOU WILL NEED TO USE TERRAFORM RESOURCE TO CREATE CLOUD SQL INSTANCE 
# EASIEST WAY IS GCLOUD OR CONSOLE 

glcoud sql instance create mysql-instance \
--database-version=MYSQL_5_7 \
-- tier=db-g1-small \
--region=us-central1 \
--root-password=jesse123 \
--availability-type=zonal  \
--storage-size=10GB \
--storage-type=HDD 


