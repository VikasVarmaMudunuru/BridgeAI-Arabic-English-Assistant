# sentiment.py
# Handles sentiment detection for BridgeAI
# Uses DistilBERT for English and CAMeL-BERT for Arabic

from transformers import pipeline
from langdetect import detect

# -------------------------------------------------------
# Load both sentiment models when the server starts
# DistilBERT  → English sentiment (positive/negative)
# CAMeL-BERT  → Arabic sentiment (trained on Gulf dialect)
# -------------------------------------------------------

print("Loading English sentiment model...")
english_sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

print("Loading Arabic sentiment model...")
arabic_sentiment = pipeline(
    "sentiment-analysis",
    model="CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
)

print("Sentiment models ready!")


def get_sentiment(text: str) -> dict:
    """
    Detects sentiment of input text.
    Auto-detects language and uses the correct model.

    Args:
        text: Input text in Arabic or English

    Returns:
        dict with keys: text, language, sentiment, confidence
    """

    # Detect language to route to correct model
    try:
        lang = detect(text)
    except:
        lang = "en"

    # Run sentiment analysis with correct model
    if lang == "ar":
        result = arabic_sentiment(text)[0]
    else:
        result = english_sentiment(text)[0]

    # Normalise labels — different models return different label names
    # We map everything to POSITIVE / NEGATIVE / NEUTRAL
    label = result["label"].upper()

    if label in ["LABEL_0", "NEGATIVE", "NEG"]:
        sentiment = "NEGATIVE"
        emoji = "😞"
    elif label in ["LABEL_1", "POSITIVE", "POS"]:
        sentiment = "POSITIVE"
        emoji = "😊"
    else:
        sentiment = "NEUTRAL"
        emoji = "😐"

    # Convert score from decimal (0.986) to percentage (98.6)
    confidence = round(result["score"] * 100, 1)

    return {
        "text": text,
        "language": lang,
        "sentiment": sentiment,
        "emoji": emoji,
        "confidence": confidence
    }
