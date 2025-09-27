# utils/translate.py
from deep_translator import GoogleTranslator

def translate_text(text, direction="en-de"):
    """
    Translate text between English and German.
    direction: 'en-de' or 'de-en'
    """
    if not text.strip():
        return ""

    try:
        if direction == "en-de":
            return GoogleTranslator(source='en', target='de').translate(text)
        elif direction == "de-en":
            return GoogleTranslator(source='de', target='en').translate(text)
        else:
            return text
    except Exception as e:
        return f"Error: Could not get translation from server ({e})"
