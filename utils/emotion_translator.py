from transformers import pipeline, MarianMTModel, MarianTokenizer

# Load emotion classification model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

# Load translation models
EN_DE_MODEL = 'Helsinki-NLP/opus-mt-en-de'
DE_EN_MODEL = 'Helsinki-NLP/opus-mt-de-en'

en_de_tokenizer = MarianTokenizer.from_pretrained(EN_DE_MODEL)
en_de_model = MarianMTModel.from_pretrained(EN_DE_MODEL)

de_en_tokenizer = MarianTokenizer.from_pretrained(DE_EN_MODEL)
de_en_model = MarianMTModel.from_pretrained(DE_EN_MODEL)

# Map emotion to emoji
EMOTION_EMOJIS = {
    "anger": "🔥 Angry",
    "joy": "😊 Joyful",
    "sadness": "😢 Sad",
    "fear": "😨 Fearful",
    "disgust": "🤢 Disgusted",
    "surprise": "😲 Surprised",
    "neutral": "💬 Neutral"
}

def detect_emotion(text):
    try:
        result = emotion_classifier(text)[0]
        emotion = result['label'].lower()
        return EMOTION_EMOJIS.get(emotion, "💬 Neutral")
    except:
        return "💬 Neutral"

def translate_with_emotion(text, direction='en-de'):
    if direction == 'en-de':
        tokenizer = en_de_tokenizer
        model = en_de_model
    elif direction == 'de-en':
        tokenizer = de_en_tokenizer
        model = de_en_model
    else:
        raise ValueError("Unsupported direction")

    tokens = tokenizer([text], return_tensors="pt", padding=True)
    output = model.generate(**tokens)
    translated = tokenizer.batch_decode(output, skip_special_tokens=True)[0]

    emotion = detect_emotion(text)
    return translated, emotion
