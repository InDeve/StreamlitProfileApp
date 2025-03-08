import pandas as pd

# Define chunk size (adjust based on your data)
chunk_size = 3_000_000  # Number of rows per chunk

# Load the CSV in chunks
csv_file = "ml_models/train_fixed.csv"

for i, chunk in enumerate(pd.read_csv(csv_file, chunksize=chunk_size)):
    chunk.to_csv(f"part_{i}.csv", index=False)