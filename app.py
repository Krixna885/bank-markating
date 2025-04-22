import streamlit as st
import pandas as pd
import zipfile
import urllib.request
import os

st.title("📊 Bank Marketing Dataset Explorer")

# Download ZIP file if not already downloaded
zip_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip'
zip_path = 'bank.zip'
csv_filename = 'bank-full.csv'

if not os.path.exists(csv_filename):
    st.info("Downloading and extracting dataset...")
    urllib.request.urlretrieve(zip_url, zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extract(csv_filename)

# Load the CSV into a DataFrame
df = pd.read_csv(csv_filename, delimiter=';')

st.success("Data loaded successfully!")

# Show a preview of the dataset
st.subheader("🔍 Preview of Dataset")
st.dataframe(df.head())

# Show basic stats
st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Optional: let user explore by selecting columns
st.subheader("🛠 Explore Columns")
selected_column = st.selectbox("Select a column to view unique values", df.columns)
st.write(f"Unique values in *{selected_column}*:", df[selected_column].unique())
