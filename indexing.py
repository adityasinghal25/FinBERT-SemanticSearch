import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from elasticsearch import Elasticsearch, helpers 
import uuid
from config import INDEX_NAME, FILE_PATH, SHEET_NAME, MODEL_NAME

# Elasticsearch setup
es = Elasticsearch(hosts=["http://localhost:9200"])

# Use a new index for semantic search
INDEX_NAME = "semantic_index"

# Check if index exists; if not, create it
if not es.indices.exists(index=INDEX_NAME):
    mapping = {
        "mappings": {
            "properties": {
                "description": {"type": "text"},
                "description_vector": {
                    "type": "dense_vector",
                    "dims": 768,
                    "index": True,
                    "similarity": "cosine"
                }
            }
        }
    }
    es.indices.create(index=INDEX_NAME, body=mapping)
    print(f"Index '{INDEX_NAME}' created successfully.")
else:
    print(f"Index '{INDEX_NAME}' already exists. Skipping creation.")

# Load data
df = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME)

# Load FinBERT Model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

# Function to get embeddings
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return torch.mean(outputs.last_hidden_state, dim=1).squeeze().tolist()

# Bulk indexing function
def bulk_index_data(df):
    actions = []
    for index, row in df.iterrows():
        description = row.get("description", "")
        if pd.notna(description):
            doc_id = str(uuid.uuid4())
            description_vector = get_embedding(description)
            action = {
                "_op_type": "index",
                "_index": INDEX_NAME,
                "_id": doc_id,
                "_source": {
                    "description": description,
                    "description_vector": description_vector
                }
            }
            actions.append(action)
    
    if actions:
        helpers.bulk(es, actions)
        print(f"Successfully indexed {len(actions)} documents.")
    else:
        print("No valid descriptions to index.")

# Indexing process
bulk_index_data(df)
