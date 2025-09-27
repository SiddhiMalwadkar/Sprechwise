import os
from flask import Flask, render_template, request
import fitz  # PyMuPDF
from textblob import TextBlob
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from rake_nltk import Rake

# NLP utils
from utils.translate import translate_text
from utils.grammar_fix import enhance_text
import language_tool_python
from flask import Flask, render_template, request, jsonify
import language_tool_python
from langdetect import detect, DetectorFactory

# Ensure consistent language detection
DetectorFactory.seed = 0

app = Flask(__name__)
tool = language_tool_python.LanguageTool('de')  # German grammar checker

chat_history = []
# ---------------- Flask Setup ---------------- #
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.secret_key = "e33c8824afebfa7f567be6106df86e91d1525d23bf7d69e28ac30cd9ecb639fb"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'


# ---------------- Routes ---------------- #

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Instant Text Translator
@app.route('/text_translator', methods=['GET', 'POST'])
def text_translator():
    input_text = ""
    translated_text = ""
    source_lang = "en"

    if request.method == 'POST':
        if request.form.get('clear'):
            input_text = ""
            translated_text = ""
        else:
            input_text = request.form.get('input_text', '').strip()
            source_lang = request.form.get('source_lang', 'en')
            target_lang = 'de' if source_lang == 'en' else 'en'
            direction = f"{source_lang}-{target_lang}"

            if input_text:
                translated_text = translate_text(input_text, direction)

    return render_template(
        'instant_translator.html',
        input_text=input_text,
        translated_text=translated_text,
        source_lang=source_lang
    )

@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        score = blob.sentiment.polarity  # -1 to 1
        if score > 0:
            sentiment_result = "Positive 😊"
        elif score < 0:
            sentiment_result = "Negative 😞"
        else:
            sentiment_result = "Neutral 😐"
        result = {
            "text": text,
            "score": score,
            "sentiment": sentiment_result
        }
    return render_template('sentiment.html', result=result)
@app.route('/keywords', methods=['GET', 'POST'])
def keywords():
    extracted = []
    if request.method == 'POST':
        text = request.form['text']
        r = Rake()
        r.extract_keywords_from_text(text)
        extracted = r.get_ranked_phrases()[:15]  # Top 15 keywords
    return render_template('keywords.html', keywords=extracted)


@app.route('/pdf_translator', methods=['GET', 'POST'])
def pdf_translator():
    result = None
    if request.method == 'POST':
        file = request.files['pdf']
        action = request.form.get('action')  # 'translate' or 'summarize'
        lang = request.form.get('lang')  # 'en-de' or 'de-en'

        # Extract text from PDF
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()

        if action == 'translate':
            direction = lang  # 'en-de' or 'de-en'
            result = translate_text(text, direction)

        elif action == 'summarize':
            try:
                # Using sumy for summarization
                parser = PlaintextParser.from_string(text, Tokenizer("english"))
                summarizer = LexRankSummarizer()
                summary_sentences = summarizer(parser.document, 5)  # Top 5 sentences
                result = " ".join([str(sentence) for sentence in summary_sentences])
                if not result.strip():
                    result = "Text too short to summarize."
            except Exception as e:
                result = f"Error during summarization: {str(e)}"

    return render_template('pdf_translator.html', result=result)




# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
