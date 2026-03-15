# translate.py
# Handles all translation logic for BridgeAI
# Uses Helsinki-NLP models from HuggingFace for Arabic <-> English translation

from transformers import MarianMTModel, MarianTokenizer
from langdetect import detect

# -------------------------------------------------------
# Load both translation models when the server starts
# We load them once at startup so every API call is fast
# Loading takes ~30 seconds but only happens once
# -------------------------------------------------------

print("Loading Arabic → English model...")
ar_en_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ar-en")
ar_en_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-ar-en")

print("Loading English → Arabic model...")
en_ar_tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
en_ar_model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-ar")

print("Translation models ready!")


def detect_language(text: str) -> str:
    """
    Detects whether text is Arabic or English.
    Returns 'ar' for Arabic, 'en' for anything else.
    """
    try:
        return detect(text)
    except:
        # If detection fails (very short text, symbols etc), default to English
        return "en"


def translate(text: str) -> dict:
    """
    Translates text between Arabic and English automatically.
    Auto-detects the input language and routes to the correct model.

    Args:
        text: Input text in Arabic or English

    Returns:
        dict with keys: original, translated, direction, detected_language
    """

    # Step 1: detect language
    lang = detect_language(text)

    if lang == "ar":
        # Arabic detected → translate to English
        inputs = ar_en_tokenizer(text, return_tensors="pt", padding=True)
        outputs = ar_en_model.generate(**inputs)
        translated = ar_en_tokenizer.decode(outputs[0], skip_special_tokens=True)
        direction = "Arabic → English"
    else:
        # English (or other) → translate to Arabic
        inputs = en_ar_tokenizer(text, return_tensors="pt", padding=True)
        outputs = en_ar_model.generate(**inputs)
        translated = en_ar_tokenizer.decode(outputs[0], skip_special_tokens=True)
        direction = "English → Arabic"

    return {
        "original": text,
        "translated": translated,
        "direction": direction,
        "detected_language": lang
    }
