import os
import pandas as pd
import streamlit as st

folder_path = 'ml_models\\anime_data'

@st.cache_data
def load_data():
    # List all files in the folder (make sure they're sorted correctly)
    file_names = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])

    # List to store DataFrames
    dfs = []

    # Loop through each file and append the DataFrame
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        dfs.append(df)

    # Concatenate all DataFrames into one
    full_df = pd.concat(dfs, ignore_index=True)
    return full_df