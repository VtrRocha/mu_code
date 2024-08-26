import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("dataset\customer reviews.csv")
df_books = pd.read_csv("dataset\Top-100 Trending Books.csv")

price_max = df_books["book price"].max()
price_min = df_books["book price"].min()

max_price = st.sidebar.slider("Price Range",price_max,price_min)
book_df = df_books[df_books["book price"] <= max_price]

book_df

fig = px.bar(book_df["year of publication"].value_counts())
fig2 = px.histogram(book_df["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig)
col2.plotly_chart(fig2)
