import os
import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
conn = sqlite3.connect("../ecommerce.db")
customer_base = pd.read_sql_query("SELECT * FROM customer_base", conn)
if "churn" not in customer_base.columns:
    customer_base["churn"] = (customer_base["frequency"] == 1).astype(int)


# KPIs
total_customers = customer_base.shape[0]
churn_rate = customer_base["churn"].mean() * 100
repeat_pct = (customer_base["frequency"] > 1).mean() * 100

st.title("Customer Retention KPI Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", total_customers)
col2.metric("Churn Rate (%)", round(churn_rate, 2))
col3.metric("Repeat Customers (%)", round(repeat_pct, 2))

# No filter
customer_base = pd.read_sql_query("SELECT * FROM customer_base", conn)
st.write(customer_base.head())

# Charts
st.subheader("Monetary Distribution")

fig = plt.figure()
plt.hist(customer_base["monetary"])
st.pyplot(fig)

st.subheader("Recency Days")

fig2 = plt.figure()
plt.hist(customer_base["recency_days"])
st.pyplot(fig2)

min_score, max_score = st.slider(
    "Average Review Score Range",
    0.0, 5.0, (1.0, 4.0)
)

filtered = customer_base[
    customer_base["avg_review_score"].between(min_score, max_score)
]

st.write(filtered.head())

status = st.selectbox("Select Churn Status", ["All", "Churned", "Active"])

if status == "Churned":
    filtered = customer_base[customer_base["churn"] == 1]
elif status == "Active":
    filtered = customer_base[customer_base["churn"] == 0]
else:
    filtered = customer_base

st.write(filtered.head())


