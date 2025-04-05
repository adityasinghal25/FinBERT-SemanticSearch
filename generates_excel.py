import pandas as pd

# Generate sample data for sample_index_data.xlsx
data_indexing = {
    "description": [
        "This is a sample description about mining services.",
        "Another text entry describing financial services.",
        "A third entry with some random information."
    ]
}
df_indexing = pd.DataFrame(data_indexing)
df_indexing.to_excel("sample_index_data.xlsx", sheet_name="IndexData", index=False)
print("sample_index_data.xlsx created with sheet 'IndexData'.")

# Generate sample data for sample_keyword_data.xlsx
data_search = {
    "Keywords": [
        "Mining Services",
        "Financial services",
        "Random information"
    ]
}
df_search = pd.DataFrame(data_search)
df_search.to_excel("sample_keyword_data.xlsx", sheet_name="Keywords", index=False)
print("sample_keyword_data.xlsx created with sheet 'Keywords'.")
