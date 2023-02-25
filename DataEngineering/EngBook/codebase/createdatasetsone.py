from google.cloud import bigquery 
from google.cloud.exceptions import NotFound 

client = bigquery.Client() 

datasets = [
    {'name': 'raw_bikesharing', 'location': 'US'},
    {'name': 'dwh_bikesharing', 'location': 'US'},
    {'name': 'dm_bikesharing', 'location': 'US'},
]

# location is now flexible 
def create_bigquery_dataset(dataset_name, location): 
    """Create a BigQuery dataset. Check if the dataset exists.

    Args:
        dataset_name (str): The name of the dataset.
        location (str): The location of the dataset.
    """
    # Input validation 
    if not dataset_name: 
        raise ValueError("Dataset name must be provided.") 
    if not location: 
        raise ValueError("Location must be provided.")
    if "-" not in location: 
        raise ValueError("Location should be in the format 'region-zone', eg.g. 'US-CENTRAL1'") 
    
    dataset_id = f"{client.project}.{dataset_name}" 
    # error handling 
    try: 
        client.get_dataset(dataset_id) 
        print(f"Dataset {dataset_id} already exists.")
    except NotFound: 
        dataset = bigquery.Dataset(dataset_id) 
        dataset.location = location 
        dataset = client.create_dataset(dataset, timeout=30)
        print(f"Created dataset {dataset_id}.")

for dataset in datasets: 
    create_bigquery_dataset(dataset['name'], dataset['location'])