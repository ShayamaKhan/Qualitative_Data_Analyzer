# Updated Code 
import os # Handle files and regular expressions.
import re # Handle files and regular expressions.
import pdfplumber # Extract text from PDF files.
import nltk # Natural Language Toolkit for text processing.
from openai import OpenAI  # OpenAI client for API calls.
from keys import open_ai_api_key # Import your OpenAI API key from a separate file.

nltk.download('punkt') # Download the punkt tokenizer for sentence tokenization.
from nltk.tokenize import sent_tokenize # Tokenize text into sentences.

client = OpenAI(api_key=open_ai_api_key) # Set up the OpenAI client with your API key

def extract_text_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def find_sentences_with_keyword_AI(text, keyword, client): 
    """
    Uses OpenAI's GPT model to extract all sentences containing the keyword from the provided text.
    """
    prompt = "".join([
        f"Extract all sentences from the following text that contain the keyword: {keyword}\n\n",
        "Text:\n",
        text])
    
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a helpful library assistant",
        input=prompt,
        temperature=0
    )
    return response.output_text 

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

def classify_tone_of_sentence(sentence, author_sentence, client):
    """
    Uses OpenAI to classify the tone of a sentence with respect to an author statement.
    """
    prompt = "".join([
        f"Classify the tone of the following sentence with respect to the statement: {author_sentence}\n\n",
        "There are three possible tones:\n",
        "1. Supportive: The sentence affirms or supports the presence of an effect, relationship, or influence of the keyword. assert or affirm the presence of an effect, relationship, or influence of the keyword on cybersickness. This tone often suggests that the factor matters, has a notable impact, or is a key contributor. Keywords include: significant, critical, affects, influences, predicts, correlated with, plays a role, associated with, linked to, worsens, improves, highly sensitive to, strong relationship, results indicate, was found to contribute, etc\n\n",
        "2. Neutral: The sentence mentions the keyword without taking a stance. Keywords include: measured, included, collected, considered, recorded, examined, controlled for, reported\n\n",
        "3. Opposing: indicates that no effect was found, no significant relationship, or even contradictory evidence between the keyword and cybersickness. The tone suggests the factor does not matter, is inconclusive, or shows inconsistent findings and uses negative phrases such as no significant, not related, was not found, did not affect, no difference, not associated, no clear pattern, mixed results, results were inconclusive, failed to show, inconsistent findings\n",
        sentence,
        "\n\nRespond with: Supportive, Neutral, or Opposing, and explain why."
    ])

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a helpful academic tone analysis assistant.",
        input=prompt,
        temperature=0
    )

    return response.output_text.strip()


# Hardcoded PDF file and keyword
pdf = "PDF 1"
keyword = "Gender"

# Extract text from the PDF (or load from cache)
if not os.path.exists("text1.txt"):
    text1 = extract_text_pdfplumber(pdf)
    with open("text1.txt", "w", encoding="utf-8") as f:
        f.write(text1)
else:
    with open("text1.txt", "r", encoding="utf-8") as f:
        text1 = f.read()

# Use OpenAI to find sentences with the keyword in the extracted text
keyword_sentences = find_sentences_with_keyword_AI(text1, keyword, client)

# Clean and split the AI-extracted sentences
cleaned = clean_pdf_text(keyword_sentences)
sentences = sent_tokenize(cleaned)

# Author's statement for tone analysis
author_sentence = "gender has an impact on the level of cybersickness experienced by users of immersive technology"

# Save sentences with tone analysis to a file
with open("sentences_with_tone.txt", "w", encoding="utf-8") as f:
    for i, sentence in enumerate(sentences):
        print(f"Sentence {i+1}: {sentence}", file=f)
        tone = classify_tone_of_sentence(sentence, author_sentence, client)
        print(tone, "\n", file=f)
        print(f"Sentence {i+1}: {sentence}")
        print(tone, "\n")