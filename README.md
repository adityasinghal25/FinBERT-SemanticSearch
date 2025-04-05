# FinBERT-SemanticSearch Application

This repository contains a semantic search application that leverages the FinBERT model to generate vector embeddings for text data and performs semantic search using Elasticsearch. The project is composed of the following Python scripts:

- **config.py:** Contains configuration settings such as the index name, Excel file paths, sheet names, and the FinBERT model name.
- **indexing.py:** Reads data from an Excel file, computes embeddings using FinBERT, and indexes the documents into Elasticsearch.
- **search.py:** Loads query keywords from an Excel file, converts them into embeddings, performs a semantic search against the indexed data, and saves the best matching document along with its similarity score into a new Excel file.
- **generates_excel.py:** Generates sample Excel files for both indexing and search purposes.
- **delete_index.py:** (Optional) Deletes the existing Elasticsearch index, useful for resetting the index during development.

## Prerequisites

- **Python 3.7+**
- **Elasticsearch:** Download and install Elasticsearch from [elastic.co](https://www.elastic.co/downloads/elasticsearch) and ensure it is running on `http://localhost:9200`.  
- **Internet Connection:** Needed for downloading the FinBERT model if not already cached.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/FinBERT-SemanticSearch.git
   cd FinBERT-SemanticSearch
