import streamlit as st
from utils.nlp_engine import TextAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import time

# Page Configuration
st.set_page_config(
    page_title="AI Text Insights",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("Configuration")
st.sidebar.info("This dashboard demonstrates NLP capabilities using Python. In a real-world scenario, this would connect to OpenAI GPT-4 or Anthropic Claude.")
model_choice = st.sidebar.selectbox("Select Model (Mock)", ["GPT-4o", "Claude 3.5 Sonnet", "Llama 3"])

# Main Content
st.title("🤖 AI Text Insights Dashboard")
st.markdown("### Analyze customer feedback, reviews, or articles instantly.")

# Input Area
text_input = st.text_area("Enter text to analyze:", height=150, placeholder="Paste your text here (e.g., product review, email content)...")

if st.button("Analyze Text"):
    if text_input:
        with st.spinner("Processing with AI..."):
            # Simulate processing delay
            time.sleep(1)
            
            # Perform Analysis
            sentiment, score = TextAnalyzer.get_sentiment(text_input)
            word_count = TextAnalyzer.get_word_count(text_input)
            keywords = TextAnalyzer.extract_keywords(text_input)
            
            # Display Metrics
            col1, col2, col3 = st.columns(3)
            col1.metric("Sentiment", sentiment, f"{score:.2f}")
            col2.metric("Word Count", word_count)
            col3.metric("Keywords Found", len(keywords))
            
            # Visualizations
            st.divider()
            c1, c2 = st.columns([2, 1])
            
            with c1:
                st.subheader("Key Topics Detected")
                if keywords:
                    st.write(", ".join([f"**{k}**" for k in keywords[:10]]))
                else:
                    st.write("No specific topics detected.")
                    
            with c2:
                st.subheader("Confidence Score")
                # Mock chart
                fig, ax = plt.subplots(figsize=(4, 3))
                ax.bar(["Positive", "Negative", "Neutral"], [abs(score) if score > 0 else 0.1, abs(score) if score < 0 else 0.1, 1-abs(score)], color=['green', 'red', 'gray'])
                st.pyplot(fig)

            # JSON Output (API Style)
            st.divider()
            with st.expander("View Raw JSON Response"):
                st.json({
                    "text_snippet": text_input[:50] + "...",
                    "analysis": {
                        "sentiment": sentiment,
                        "polarity": score,
                        "keywords": keywords
                    },
                    "meta": {
                        "model": model_choice,
                        "timestamp": pd.Timestamp.now().isoformat()
                    }
                })
    else:
        st.warning("Please enter some text to analyze.")

# Footer
st.markdown("---")
st.markdown("Created for Upwork Portfolio Demonstration | Python + Streamlit + NLP")
