# utils/summarize.py

def summarize_text(text):
    """
    Summarize the input text.
    Currently a placeholder: returns first 100 characters.
    Replace with real NLP summarization logic.
    """
    return text[:100] + "..." if len(text) > 100 else text