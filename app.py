import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt

# Initialize AI analyzer
analyzer = pipeline("sentiment-analysis")

# Streamlit dashboard
st.title("🧠 Nexora Intelligence AI Dashboard")
st.write("Analyze multiple texts instantly using AI intelligence.")

# Input area
st.subheader("Enter your text (one sentence per line):")
user_input = st.text_area("Type or paste text here...", "AI is the future.\nWar causes suffering.\nThe weather is fine today.")

# Analyze button
if st.button("Analyze"):
    # Split input into lines
    texts = [line.strip() for line in user_input.split("\n") if line.strip()]
    
    # Run AI analysis
    results = analyzer(texts)
    
    # Create DataFrame for results
    df = pd.DataFrame(results)
    df.insert(0, "Text", texts)
    
    # Display table
    st.subheader("🧩 Analysis Results")
    st.dataframe(df)
    
    # Visualization
    st.subheader("📊 Sentiment Overview")
    sentiment_counts = df['label'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.index, sentiment_counts.values)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    ax.set_title("Sentiment Distribution")
    st.pyplot(fig)
    
    st.success("✅ Analysis complete! Powered by Nexora Intelligence AI.")

