import streamlit as st

from pipeline import run_pipeline


st.title("Automated Data Quality & Imputation Pipeline")

file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:
    with open("temp.csv", "wb") as f:
        f.write(file.getbuffer())

    run_pipeline("temp.csv")

    st.success("Dataset cleaned successfully!")

    st.download_button("Download Clean Data", open("clean_data.csv", "rb"))
