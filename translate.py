# translate.py
# Uses MyMemory free translation API (no model loading, no memory issues)
import requests
from langdetect import detect

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "en"

def translate(text: str) -> dict:
    lang = detect_language(text)

    if lang == "ar":
        direction = "Arabic → English"
        lang_pair = "ar|en"
    else:
        direction = "English → Arabic"
        lang_pair = "en|ar"

    response = requests.get(
        "https://api.mymemory.translated.net/get",
        params={"q": text, "langpair": lang_pair}
    )
    result = response.json()
    translated = result["responseData"]["translatedText"]

    return {
        "original": text,
        "translated": translated,
        "direction": direction,
        "detected_language": lang
    }
```

---

## Also update `requirements.txt`

Remove the heavy libraries. Replace the whole file with:
```
fastapi
uvicorn
pydantic
langdetect
requests
transformers
torch
sentencepiece
