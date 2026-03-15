# main.py
# FastAPI backend for BridgeAI
# This file creates the web API that the frontend will call
# Run with: uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from translate import translate, detect_language
from sentiment import get_sentiment

# -------------------------------------------------------
# Create the FastAPI app
# FastAPI automatically creates documentation at /docs
# Visit http://localhost:8000/docs to test your API
# -------------------------------------------------------
app = FastAPI(
    title="BridgeAI API",
    description="Arabic ↔ English Translation + Sentiment Analysis",
    version="1.0.0"
)

# -------------------------------------------------------
# CORS middleware — allows the frontend (HTML page) to
# call this API even though they're on different ports
# Without this, browsers block the requests for security
# -------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows all origins (fine for development)
    allow_methods=["*"],  # allows GET, POST, PUT etc
    allow_headers=["*"],  # allows all headers
)

# -------------------------------------------------------
# Request models — defines what data the API expects
# Pydantic validates the input automatically
# If someone sends wrong data type, FastAPI returns error
# -------------------------------------------------------
class TextInput(BaseModel):
    text: str  # the input text from the user


# -------------------------------------------------------
# API ENDPOINTS
# Each function below becomes a URL the frontend can call
# -------------------------------------------------------

@app.get("/")
def root():
    """Health check — confirms the API is running"""
    return {
        "status": "running",
        "message": "BridgeAI API is live!",
        "endpoints": ["/translate", "/sentiment", "/analyze"]
    }


@app.post("/translate")
def translate_text(input: TextInput):
    """
    Translates text between Arabic and English.
    Auto-detects input language.

    Send: { "text": "Hello how are you?" }
    Get:  { "original": "...", "translated": "...", "direction": "..." }
    """
    result = translate(input.text)
    return result


@app.post("/sentiment")
def analyze_sentiment(input: TextInput):
    """
    Detects sentiment of input text.
    Works for both Arabic and English.

    Send: { "text": "I love Dubai!" }
    Get:  { "sentiment": "POSITIVE", "confidence": 99.8, "emoji": "😊" }
    """
    result = get_sentiment(input.text)
    return result


@app.post("/analyze")
def full_analysis(input: TextInput):
    """
    Full BridgeAI pipeline — translation + sentiment in one call.
    This is the main endpoint the frontend chat UI will use.

    Send: { "text": "مرحبا كيف حالك" }
    Get:  {
            "original": "مرحبا كيف حالك",
            "translated": "Hello how are you",
            "direction": "Arabic → English",
            "sentiment_original": "POSITIVE",
            "sentiment_original_confidence": 97.2,
            "sentiment_translated": "POSITIVE",
            "sentiment_translated_confidence": 99.1
          }
    """
    # Step 1: translate
    translation = translate(input.text)

    # Step 2: sentiment on original text
    sentiment_original = get_sentiment(input.text)

    # Step 3: sentiment on translated text
    sentiment_translated = get_sentiment(translation["translated"])

    return {
        "original": input.text,
        "translated": translation["translated"],
        "direction": translation["direction"],
        "detected_language": translation["detected_language"],
        "sentiment_original": sentiment_original["sentiment"],
        "sentiment_original_emoji": sentiment_original["emoji"],
        "sentiment_original_confidence": sentiment_original["confidence"],
        "sentiment_translated": sentiment_translated["sentiment"],
        "sentiment_translated_emoji": sentiment_translated["emoji"],
        "sentiment_translated_confidence": sentiment_translated["confidence"],
    }
