import streamlit as st
from functions.plot import plot_ts

st.title("O nomezinho muito brabo")
st.write("DAAAAAAAAAAAAAAAAAAAAAAAAMN")

ticker = st.sidebar.text_input("Escolhe aí menó", value="AAPL")

fig = plot_ts(ticker)

st.plotly_chart(fig)

# what???