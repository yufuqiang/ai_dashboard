from textblob import TextBlob
import re

class TextAnalyzer:
    @staticmethod
    def get_sentiment(text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        
        if sentiment_score > 0.1:
            return "Positive", sentiment_score
        elif sentiment_score < -0.1:
            return "Negative", sentiment_score
        else:
            return "Neutral", sentiment_score

    @staticmethod
    def get_word_count(text):
        return len(text.split())

    @staticmethod
    def clean_text(text):
        # Simple cleaning
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    @staticmethod
    def extract_keywords(text):
        # Mocking keyword extraction with Nouns
        blob = TextBlob(text)
        return list(set(blob.noun_phrases))
