# utils/translate.py
from transformers import MarianMTModel, MarianTokenizer


def get_model_and_tokenizer(direction):
    if direction == "en-de":
        model_name = "Helsinki-NLP/opus-mt-en-de"
    elif direction == "de-en":
        model_name = "Helsinki-NLP/opus-mt-de-en"
    else:
        raise ValueError("Unsupported direction")

    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer


def translate_text(text, direction):
    model, tokenizer = get_model_and_tokenizer(direction)
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
