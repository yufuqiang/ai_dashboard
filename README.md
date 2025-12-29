# AI Text Insights Dashboard

A modern, interactive web application built with Streamlit that demonstrates NLP (Natural Language Processing) capabilities. This project serves as a template for building internal tools, AI wrappers, and data dashboards.

## 🚀 Features

-   **Interactive UI**: Built with Streamlit for rapid deployment and ease of use.
-   **Sentiment Analysis**: Automatically detects positive, negative, or neutral tones in text.
-   **Keyword Extraction**: Identifies key topics and noun phrases.
-   **Real-time Visualization**: Dynamic charts updating based on user input.
-   **Modular Design**: Logic is separated into `utils/nlp_engine.py`, making it easy to swap in real LLM APIs (OpenAI/Anthropic).

## 📂 Project Structure

```
ai_dashboard/
├── utils/
│   └── nlp_engine.py    # Core text processing logic
├── data/                # Data storage (if needed)
├── app.py               # Streamlit application entry point
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## ⚡ Quick Start

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the App**:
    ```bash
    streamlit run app.py
    ```

3.  **Access Dashboard**:
    Open your browser at `http://localhost:8501`.

## 💼 Business Case

This type of dashboard is highly requested on Upwork for:
-   **Customer Support**: Analyzing ticket sentiment to prioritize angry customers.
-   **Marketing**: Testing ad copy effectiveness before launch.
-   **Product**: Summarizing user reviews from Amazon or App Store.
-   **Internal Tools**: Creating interfaces for custom AI models without frontend development costs.

---
*Created for Upwork Portfolio Demonstration*
