# cultural_tips.py
# Knowledge base of Arabic cultural phrases for BridgeAI
# When these phrases are detected, the app shows a cultural context card
# This is what makes BridgeAI different from Google Translate

CULTURAL_TIPS = {
    # Greetings
    "inshallah": {
        "arabic": "إن شاء الله",
        "literal": "If God wills it",
        "cultural": "One of the most used phrases in Arabic culture. Can mean genuine hope, polite agreement, or 'maybe/we'll see' depending on tone. In UAE business culture, always follow up if you need a firm commitment.",
        "emoji": "🤲",
        "category": "Faith & Hope"
    },
    "mashallah": {
        "arabic": "ما شاء الله",
        "literal": "What God has willed",
        "cultural": "Expressed when admiring something beautiful or praising someone's achievement. Also used to ward off the evil eye. If someone compliments your work and says Mashallah, it's a very high compliment.",
        "emoji": "✨",
        "category": "Admiration"
    },
    "alhamdulillah": {
        "arabic": "الحمد لله",
        "literal": "Praise be to God",
        "cultural": "Said to express gratitude in any situation — good or bad. If someone asks 'how are you?' the response is often Alhamdulillah. It shows acceptance and thankfulness.",
        "emoji": "🙏",
        "category": "Gratitude"
    },
    "yalla": {
        "arabic": "يلا",
        "literal": "Let's go / Come on",
        "cultural": "One of the most versatile words in Gulf Arabic. Can mean 'hurry up', 'let's go', 'come on', or even 'goodbye'. The tone completely changes the meaning. Very commonly used in Dubai daily life.",
        "emoji": "🏃",
        "category": "Expression"
    },
    "habibi": {
        "arabic": "حبيبي",
        "literal": "My love / My dear",
        "cultural": "Term of endearment used between friends, family, or even strangers in a warm context. In UAE it's used casually between men as 'buddy' or 'mate'. Habibti is the female form.",
        "emoji": "❤️",
        "category": "Endearment"
    },
    "habibti": {
        "arabic": "حبيبتي",
        "literal": "My love / My dear (female)",
        "cultural": "Female form of Habibi. Used between women or by men addressing women affectionately. Very common in UAE daily conversation.",
        "emoji": "💕",
        "category": "Endearment"
    },
    "wallah": {
        "arabic": "والله",
        "literal": "By God / I swear by God",
        "cultural": "Used to emphasise truth or sincerity. 'Wallah I'm telling the truth!' Also used casually to express surprise or emphasis. Very common in informal UAE conversation.",
        "emoji": "🤝",
        "category": "Emphasis"
    },
    "bismillah": {
        "arabic": "بسم الله",
        "literal": "In the name of God",
        "cultural": "Said before starting any important task, eating, or beginning a journey. Shows intention and seeking blessing. You'll hear this constantly in UAE workplaces and homes.",
        "emoji": "🌟",
        "category": "Blessing"
    },
    "assalamu alaikum": {
        "arabic": "السلام عليكم",
        "literal": "Peace be upon you",
        "cultural": "The standard Islamic greeting. Always responded to with 'Wa alaikum assalam' (And peace be upon you too). Using this greeting in UAE shows cultural respect and awareness.",
        "emoji": "☮️",
        "category": "Greeting"
    },
    "marhaba": {
        "arabic": "مرحبا",
        "literal": "Hello / Welcome",
        "cultural": "A warm, casual hello used across the Arab world. Response is 'Marhabtain' (double welcome). More casual than Assalamu Alaikum but equally warm.",
        "emoji": "👋",
        "category": "Greeting"
    },
    "shukran": {
        "arabic": "شكراً",
        "literal": "Thank you",
        "cultural": "The standard thank you. Response is 'Afwan' (you're welcome). Adding 'Jazeelan' makes it 'Thank you very much'. Always appreciated when expats use it in UAE.",
        "emoji": "🙏",
        "category": "Gratitude"
    },
    "afwan": {
        "arabic": "عفواً",
        "literal": "You're welcome / Excuse me",
        "cultural": "Used both as 'you're welcome' after being thanked, and as 'excuse me' to get someone's attention politely. Context determines the meaning.",
        "emoji": "😊",
        "category": "Courtesy"
    },
    "khalas": {
        "arabic": "خلاص",
        "literal": "Done / Finished / Enough",
        "cultural": "Extremely common in UAE. Means something is done, settled, or finished. 'Khalas, let's move on' is heard in every Dubai office. Can also mean 'stop' or 'enough' in an argument.",
        "emoji": "✅",
        "category": "Expression"
    },
    "mabrook": {
        "arabic": "مبروك",
        "literal": "Congratulations / Blessed",
        "cultural": "Said to congratulate someone on good news — a promotion, marriage, new baby, new home. Response is 'Allah yubarak feek' (May God bless you too). Very important in UAE social culture.",
        "emoji": "🎉",
        "category": "Celebration"
    },
    "sabah al khair": {
        "arabic": "صباح الخير",
        "literal": "Good morning",
        "cultural": "The morning greeting. Response is 'Sabah al noor' (Morning of light). These formal greetings are important in UAE business settings — using them shows cultural respect.",
        "emoji": "🌅",
        "category": "Greeting"
    },
    "tfaddal": {
        "arabic": "تفضل",
        "literal": "Please / Go ahead / Help yourself",
        "cultural": "One of the most hospitable words in Arabic. Used to invite someone in, offer food, or say 'after you'. Hospitality (Diyafa) is central to Emirati culture and Tfaddal embodies it.",
        "emoji": "🤗",
        "category": "Hospitality"
    }
}


def get_cultural_tip(text: str) -> dict | None:
    """
    Checks if the input text contains a known Arabic cultural phrase.
    Returns the cultural tip if found, None if not.

    Args:
        text: Input text to check

    Returns:
        dict with cultural tip info, or None if no match found
    """
    text_lower = text.lower().strip()

    # Check each phrase in our knowledge base
    for phrase, tip in CULTURAL_TIPS.items():
        if phrase in text_lower:
            return {
                "phrase": phrase,
                "arabic": tip["arabic"],
                "literal": tip["literal"],
                "cultural": tip["cultural"],
                "emoji": tip["emoji"],
                "category": tip["category"]
            }

    # Also check Arabic script directly
    for phrase, tip in CULTURAL_TIPS.items():
        if tip["arabic"] in text:
            return {
                "phrase": phrase,
                "arabic": tip["arabic"],
                "literal": tip["literal"],
                "cultural": tip["cultural"],
                "emoji": tip["emoji"],
                "category": tip["category"]
            }

    return None