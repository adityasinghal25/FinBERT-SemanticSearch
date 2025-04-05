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

 2. **Install Required Python Libraries:**

    ```bash
    pip install pandas torch transformers elasticsearch openpyxl

## Usage

1. **Generate Sample Excel Files:**Run the generates_excel.py script to create sample Excel files for indexing and searching.

   **This will create:**
      - sample_index_data.xlsx with a sheet named IndexData containing sample descriptions.
      - sample_keyword_data.xlsx with a sheet named Keywords containing sample query keywords

3. **Index Data into Elasticsearch:** Run the indexing.py script to index data from sample_index_data.xlsx into Elasticsearch.

    **The script:**
      - checks if the index exists and, if not, create it with the required mapping.
      - processes each description, computes its FinBERT embedding, and bulk indexes the documents.
  
4. **Perform Semantic Search:** Run the search.py script to perform a semantic search using keywords from sample_keyword_data.xlsx.

     **The script:**
      - generates embeddings for each query keyword, performs a semantic search against the indexed documents.
      -  saves the best match along with its similarity score into a new Excel file (with a modified name).
  
5. **(Optional) Delete Existing Elasticsearch Index:** If you wish to clear the current index before re-indexing, run the delete_index.py script.


## Troubleshooting

1. Elasticsearch Connection Issues:
Make sure Elasticsearch is running at http://localhost:9200. You can adjust the host and port in the scripts if necessary.

2. Timeouts or Performance Issues:
If you encounter connection timeouts, consider increasing the timeout settings in the Elasticsearch client initialization in your scripts.

3. Disk Space Warnings:
If Elasticsearch warns about disk usage (e.g., high disk watermark), ensure you have sufficient free space or adjust the watermark settings in elasticsearch.yml for development purposes.
      

## Acknowledgements

1. FinBERT by ProsusAI.
2. Elasticsearch
3. Transformers

