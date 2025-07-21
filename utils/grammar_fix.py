# utils/grammar_fix.py

from transformers import pipeline

# Load grammar correction model (small and effective)
grammar_corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

def enhance_text(text, tone='formal', vocab_level='intermediate'):
    from transformers import pipeline

    # You may load a fine-tuned grammar model or use any grammar correction logic
    corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

    enhanced = corrector(text, max_length=512, do_sample=False)[0]['generated_text']

    # Simulate vocabulary/tone transformation (you can integrate OpenAI API or another model here)
    enhanced += f" [Tone adjusted to: {tone.capitalize()}, Vocabulary: {vocab_level.capitalize()}]"

    # Dummy grammar explanations (for real use, plug in LanguageTool or similar)
    explanations = [
        "Corrected verb tense in sentence 2.",
        "Improved punctuation and article usage.",
    ]

    return enhanced, explanations

