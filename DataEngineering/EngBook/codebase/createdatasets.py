from google.cloud import bigquery
from google.cloud.exceptions import NotFound

# this method creates a new client object that is used to interact with the BigQuery API 
client = bigquery.Client()

# list contains the names of the datasets that the code will create 
datasets_name = ['raw_bikesharing','dwh_bikesharing','dm_bikesharing']
# where the dataset will be created 
location = 'US'

# function creates a new dataset if it does not exist
def create_bigquery_dataset(dataset_name):
    """Create bigquery dataset. Check first if the dataset exists
        Args:
            dataset_name: String
    """

    dataset_id = "{}.{}".format(client.project, dataset_name)
    try:
        # tries to get the dataset using get_dataset method 
        client.get_dataset(dataset_id)
        print("Dataset {} already exists".format(dataset_id))
        # if it does not exist creates a new dataset using bigquery.Dataset() method and 
        # sets its location to the specified location 
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location
        # create dataset method 
        dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
        print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


for name in datasets_name:
    create_bigquery_dataset(name)