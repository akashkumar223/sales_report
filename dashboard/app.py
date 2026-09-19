import streamlit as st
import pandas as pd

st.set_page_config(page_title="Superstore Analytics", layout="wide")
df = pd.read_csv("../data/cleaned_superstore.csv", encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"])

st.title("📊 Superstore Sales Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Total Orders", df["Order ID"].nunique())

st.subheader("Sales by Category")
st.bar_chart(df.groupby("Category")["Sales"].sum())

st.subheader("Profit by Region")
st.bar_chart(df.groupby("Region")["Profit"].sum())

st.subheader("Monthly Sales Trend")
monthly = df.groupby(df["Order Date"].dt.to_period("M").astype(str))["Sales"].sum()
st.line_chart(monthly)

st.subheader("Top 10 Products by Sales")
st.dataframe(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))