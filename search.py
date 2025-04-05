# search.py

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from elasticsearch import Elasticsearch
from config import INDEX_NAME, MODEL_NAME, FEATURES_FILE_PATH, FEATURES_SHEET_NAME

# Elasticsearch client
es = Elasticsearch(hosts=["http://localhost:9200"])

# Load FinBERT Model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

# Embedding function
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return torch.mean(outputs.last_hidden_state, dim=1).squeeze().tolist()

# Semantic search function
def semantic_search(query, top_k=1):
    query_vector = get_embedding(query)
    search_query = {
        "size": top_k,
        "query": {
            "script_score": {
                "query": {
                    "match_all": {}
                },
                "script": {
                    "source": """
                        double vector_score = cosineSimilarity(params.query_vector, 'description_vector');
                        return vector_score;
                    """,
                    "params": {
                        "query_vector": query_vector
                    }
                }
            }
        }
    }

    response = es.search(index=INDEX_NAME, body=search_query)
    hits = response["hits"]["hits"]
    if hits:
        return hits[0]["_source"]["description"], hits[0]["_score"]
    return "No match found", 0.0

# Load features Excel (with Keywords)
df = pd.read_excel(FEATURES_FILE_PATH, sheet_name=FEATURES_SHEET_NAME)

# Process each query and save closest output with score
results = df["Keywords"].apply(lambda x: semantic_search(x) if pd.notna(x) else (None, 0.0))
df["Closest Output"] = results.apply(lambda x: x[0])
df["Semantic Score"] = results.apply(lambda x: x[1])

# Save updated Excel file
output_path = FEATURES_FILE_PATH.replace(".xlsx", "_with_closest_output_and_score.xlsx")
df.to_excel(output_path, index=False)

print(f"Updated file saved as {output_path}")
