import streamlit as st
from data_seed import seed_portfolio
from utils import calc_expected_value

st.set_page_config(layout="wide")

st.title("Junior Mining Portfolio Dashboard")

if "portfolio_df" not in st.session_state:
    st.session_state.portfolio_df = seed_portfolio()

df = st.session_state.portfolio_df

st.subheader("Portfolio Table")

edited = st.data_editor(df, use_container_width=True)

if not edited.empty:
    edited["Expected Value"] = [
        calc_expected_value(s, u)
        for s, u in zip(edited["Score"], edited["Upside (x)"])
    ]

st.dataframe(edited, use_container_width=True)

if st.button("Save"):
    st.session_state.portfolio_df = edited
