import streamlit as st
import pandas as pd

st.title("📊 Smart Data Pipeline Dashboard")

df = pd.read_csv("data/sample_data.csv")
anomalies = pd.read_csv("data/anomalies.csv")

st.subheader("Transaction Amount Trend")
st.line_chart(df["amount"])

st.subheader("Detected Anomalies")
st.write(anomalies)
