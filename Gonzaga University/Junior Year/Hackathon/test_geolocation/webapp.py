import streamlit as st
import json

st.title('Ski Resort Information')

tabMain, tabInfo = st.tabs(["Main", "Info"])
col1, col2 = st.columns(["Weather", "Distance"])

with tabMain:
    st.subheader("Search for resorts")
    search = st.text_input("Resort Name")
    curLocation = st.button("Locate Me")

    with col1:
        weather = st.text_area("Check Weather")

    with col2:
        distance = st.text_area("Choose your distance")