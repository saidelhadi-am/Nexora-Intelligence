import streamlit as st
from transformers import pipeline

# Initialize AI analyzer
analyzer = pipeline("sentiment-analysis")

st.title("Nexora Intelligence AI Dashboard")
st.write("Analyze text with AI instantly!")

user_input = st.text_area("Enter text for analysis:", "Type your text here...")

if st.button("Analyze"):
    result = analyzer(user_input)
    st.write("AI Analysis Result:", result)
