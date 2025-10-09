import streamlit as st
import pandas as pd
import sqlite3

st.title("Crypto Dashboard")

conn = sqlite3.connect("database/crypto_data.db")
df = pd.read_sql("SELECT * FROM crypto_prices ORDER BY extracted_at DESC", conn)
conn.close()

st.dataframe(df)

top = df.groupby("id").tail(1).sort_values("market_cap", ascending=False)
st.bar_chart(top.set_index("id")["current_price"])
