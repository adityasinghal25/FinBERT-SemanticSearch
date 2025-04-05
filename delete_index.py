#Optional File
from elasticsearch import Elasticsearch
from config import INDEX_NAME
 
# Connect to Elasticsearch with the scheme
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Delete the index
try:
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
        print(f"Index '{INDEX_NAME}' deleted successfully.")
    else:
        print(f"Index '{INDEX_NAME}' does not exist.")
except Exception as e:
    print(f"Error deleting index '{INDEX_NAME}': {e}")


