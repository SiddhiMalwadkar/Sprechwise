import os

import fitz
from flask import Flask, render_template
from flask import Flask, render_template, request
import fitz
from utils.grammar_fix import enhance_text
from utils.summarize import summarize_text
from utils.translate import translate_text
import utils.translate
from utils.emotion_translator import translate_with_emotion

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/text_translator", methods=["GET", "POST"])
def text_translator():
    translated = None
    if request.method == "POST":
        text = request.form["text"]
        direction = request.form["direction"]
        translated = utils.translate.translate_text(text, direction)
    return render_template("text_translator.html", translated=translated)


@app.route('/pdf-translator', methods=['GET', 'POST'])
def pdf_translator():
    translated = None
    summary = None

    if request.method == 'POST':
        file = request.files['pdf_file']
        direction = request.form['direction']

        if file and file.filename.endswith('.pdf'):
            path = os.path.join('uploads', file.filename)
            file.save(path)

            text = extract_text_from_pdf(path)

            if text.strip():
                translated = utils.translate.translate_text(text, direction)
                summary = summarize_text(translated)

    return render_template('pdf_translator.html', translated=translated, summary=summary)


def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text.strip()


@app.route('/emotion-translate', methods=['GET', 'POST'])
def emotion_translate():
    translated_text = ""
    emotion_tag = ""
    source_text = ""
    direction = "en-de"

    if request.method == 'POST':
        source_text = request.form["source_text"]
        direction = request.form["direction"]
        translated_text, emotion_tag = translate_with_emotion(source_text, direction)

    return render_template("emotion_translator.html", translated_text=translated_text, emotion_tag=emotion_tag, source_text=source_text)

@app.route("/region-translate", methods=["GET", "POST"])




@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
