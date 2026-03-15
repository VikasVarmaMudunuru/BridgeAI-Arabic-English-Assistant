# main.py
# FastAPI backend for BridgeAI
# Run with: uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from translate import translate, detect_language
from sentiment import get_sentiment
from cultural_tips import get_cultural_tip

app = FastAPI(
    title="BridgeAI API",
    description="Arabic ↔ English Translation + Sentiment Analysis + Cultural Tips",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "BridgeAI API is live!",
        "endpoints": ["/translate", "/sentiment", "/analyze", "/cultural"]
    }


@app.post("/translate")
def translate_text(input: TextInput):
    return translate(input.text)


@app.post("/sentiment")
def analyze_sentiment(input: TextInput):
    return get_sentiment(input.text)


@app.post("/cultural")
def cultural_tip(input: TextInput):
    tip = get_cultural_tip(input.text)
    if tip:
        return {"found": True, "tip": tip}
    return {"found": False, "tip": None}


@app.post("/analyze")
def full_analysis(input: TextInput):
    translation = translate(input.text)
    sentiment_original = get_sentiment(input.text)
    sentiment_translated = get_sentiment(translation["translated"])
    cultural = get_cultural_tip(input.text)

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
        "cultural_tip": cultural
    }
