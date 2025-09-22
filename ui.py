# streamlit_app.py
import streamlit as st
import requests

st.title("Real-Time Market Sentiment Analyzer")
company = st.text_input("Enter Company Name", value="Google")
if st.button("Analyze"):
    if company:
        with st.spinner("Fetching and analyzing news..."):
            try:
                response = requests.get(f"http://127.0.0.1:8000/analyze/?company={company}")
                data = response.json()
                st.subheader("Sentiment Profile")
                st.json(data)
            except Exception as e:
                st.error(f"Error: {e}")
