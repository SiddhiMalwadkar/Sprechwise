# Sprechwise
Sprechwise is a smart multilingual translator web application designed to bridge communication gaps between **English** and **German**.  
It goes beyond basic translation by integrating **emotion detection**, **context-aware output**, and **PDF document translation and summarization** — all built using NLP and modern web technologies.

---

## 🔧 Features

### 📝 Instant Text Translator
- Real-time translation between **English ↔ German**
- Powered by pre-trained machine translation models

### 💬 Emotion-Sensitive Translator
- Translates text with emotional tone in mind
- Detects and tags emotions like Joy, Sadness, Anger, etc.
- Enhances translation by capturing **context and mood**

### 📄 PDF Translator & Summarizer
- Upload any English/German PDF
- Automatically extracts, translates, and summarizes content
- Ideal for study notes, articles, or research material

---

## 🚀 Tech Stack

- **Frontend:** HTML5, CSS3, Jinja2 (Flask templating)
- **Backend:** Python, Flask
- **NLP Models:** Hugging Face Transformers
- **PDF Processing:** PyMuPDF (`fitz`)
- **Emotion Detection:** `j-hartmann/emotion-english-distilroberta-base`
- **Translation Models:** Helsinki-NLP MarianMT models
- **Summarization:** Pre-trained `summarization` pipeline

---

## 📁 Project Structure

```bash
Sprechwise/
│
├── app.py                     # Flask App Entry Point
├── requirements.txt           # Required packages
│
├── utils/
│   ├── emotion_translator.py  # Emotion detection + translation
│   ├── translate.py           # Basic translator logic
│   ├── summarize.py           # Summarizer logic
│
├── templates/
│   ├── index.html             # Homepage
│   ├── text_translator.html   # Instant Translator UI
│   ├── emotion_translator.html # Emotion-aware Translator UI
│   ├── pdf_translator.html    # PDF Upload & Result UI
│   ├── contact.html           # Static contact form
│
└── static/
    └── style.css              # Optional styling assets
