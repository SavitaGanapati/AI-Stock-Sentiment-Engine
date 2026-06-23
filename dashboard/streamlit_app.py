import streamlit as st

st.title("AI Stock Sentiment Engine")

st.header("Top Ranked Stocks")

stocks = [
    ("RELIANCE.NS", 82),
    ("INFY.NS", 76),
    ("TCS.NS", 71)
]

for ticker, fsi in stocks:

    st.write(
        f"{ticker} : FSI = {fsi}"
    )