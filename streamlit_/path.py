import pandas as pd

def load_data():
    df = pd.read_parquet('../data/dataset_streamlit.parquet')
    return df

