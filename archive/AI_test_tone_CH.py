import os
from tkinter import Tk, filedialog, simpledialog
import PyPDF2
import re
import pdfplumber
import tiktoken  # pip install tiktoken --upgrade

from openai import OpenAI  # pip install openai --upgrade
from keys import open_ai_api_key  # you must enter your OpenAI API key in a file called keys.py

client = OpenAI(
    api_key=open_ai_api_key
)



def classify_tone_of_sentence(sentence, author_sentence, client):
    prompt = "".join([
        f"Classify the tone of the following sentence with respect to the statement: {author_sentence}\n\n",
        "There are three possible tones:\n",
        "1. Supportive: The sentence affirms or supports the presence of an effect, relationship, or influence of the keyword. assert or affirm the presence of an effect, relationship, or influence of the keyword on cybersickness. This tone often suggests that the factor matters, has a notable impact, or is a key contributor. Keywords include: significant, critical, affects, influences, predicts, correlated with, plays a role, associated with, linked to, worsens, improves, highly sensitive to, strong relationship, results indicate, was found to contribute, etc\n\n",
        "2. Neutral: The sentence mentions the keyword without taking a stance. Keywords include: "
        "measured, included, collected, considered, recorded, examined, controlled for, reported\n\n",
        "3. Opposing: indicates that no effect was found, no significant relationship, or even contradictory evidence between the keyword and cybersickness. The tone suggests the factor does not matter, is inconclusive, or shows inconsistent findings and uses negative phrases such as no significant, not related, was not found, did not affect, no difference, not associated, no clear pattern, mixed results, results were inconclusive, failed to show, inconsistent findings\n",
        text,
        "\n\nRespond with : Supportive, Neutral, and explain why"
    ])

    response = client.responses.create(
        model="gpt-4o", #for small language tasks
        instructions="You are a helpful academic tone analysis assistant.",
        input=prompt,
        temperature=0
    )

    return response.output_text.strip()




with open("text3.txt", "r", encoding="utf-8") as f:
    text = f.read()    


import nltk
import re
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

def clean_pdf_text(text):
    # Fix hyphenated line breaks
    text = re.sub(r'(\w+)\s*-\s*\n\s*(\w+)', r'\1\2', text)
    text = text.replace('al.', 'al')
    # Remove HTML entities
    text = re.sub(r'&[a-z]+;', '', text)
    # Replace all remaining newlines with spaces
    text = text.replace('\n', ' ')
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


cleaned = clean_pdf_text(text)
sentences = sent_tokenize(cleaned)






author_sentence = "gender has an impact on the level of cybersickness experienced by users of immersive technology"

# save to text file
with open("sentences_with_tone.txt", "w", encoding="utf-8") as f:
    for i, sentence in enumerate(sentences):
        print(f"Sentence {i+1}: {sentence}", file=f)
        print(classify_tone_of_sentence(sentence, author_sentence, client), "\n", file=f)
        print(f"Sentence {i+1}: {sentence}")
        print(classify_tone_of_sentence(sentence, author_sentence, client), "\n")
