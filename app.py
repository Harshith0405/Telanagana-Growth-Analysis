import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Telangana Growth Analysis",
    layout="wide"
)

st.title("📊 Telangana Growth Analysis Dashboard")

st.write(
    "Interactive dashboard showing Telangana growth analysis using "
    "district, investment, transport and development datasets."
)

df = pd.read_csv("Telangana_final_analysis.csv")

st.subheader("Dataset Preview")
st.dataframe(df)

st.subheader("Dataset Statistics")
st.write(df.describe())

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Total Columns", len(df.columns))


numeric_columns = df.select_dtypes(
    include=["int64", "float64"]
).columns

if len(numeric_columns) > 0:

    column = st.selectbox(
        "Select column for visualization",
        numeric_columns
    )

    fig, ax = plt.subplots()

    df[column].plot(
        kind="bar",
        ax=ax
    )

    st.pyplot(fig)