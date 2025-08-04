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
#models = client.models.list()
#for model in models.data:
#   print(model.id)

def find_sentences_with_keyword_AI(text, keyword, client): 
    prompt = "".join([
        f"Extract all sentences from the following text that contain the keyword:{keyword}\n\n",
        "Text:\n",
        text])
    

    response = client.responses.create(
        model="gpt-4o-mini",  # cheapest model for this task, long text
        instructions="You are a helpful library assistant",
        input=prompt,
        temperature=0  # do not be creative!
    )

    result = response.output_text 
    return result  

def convert_with_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber."""
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
            print(".", end="", flush=True)  # Print a dot for each page processed
    return text

def convert_with_pypdf2(pdf_path):
    """Extract text from PDF using PyPDF2."""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
            print(".", end="", flush=True)
    return text

####################################

pdf = "Identifying Causes of and Solutions for Cybersickness in Immersive Technology Reformulation of a Research and Development Agenda.pdf"
keyword = "cybersickness"

if not os.path.exists("text1.txt"):
    text1 = convert_with_pdfplumber(pdf)
    with open("text1.txt", "w", encoding="utf-8") as f:
        f.write(text1)
else:
    with open("text1.txt", "r", encoding="utf-8") as f:
        text1 = f.read()

if not os.path.exists("text2.txt"):
    text2 = convert_with_pypdf2(pdf) # much faster and generates more text (?)
    with open("text2.txt", "w", encoding="utf-8") as f:
        f.write(text2)
else:
    with open("text2.txt", "r", encoding="utf-8") as f:
        text2 = f.read()    

encoding = tiktoken.encoding_for_model("gpt-4o-mini")
num_tokens = len(encoding.encode(text1))
print("text2", num_tokens)

encoding = tiktoken.encoding_for_model("gpt-4o-mini")
num_tokens = len(encoding.encode(text2))
print("text1", num_tokens)

# find sentences with keyword using AI
result1 = find_sentences_with_keyword_AI(text1, keyword, client)
result2 = find_sentences_with_keyword_AI(text2, keyword, client)

# save the results to a file
with open("result1.txt", "w", encoding="utf-8") as f:
    f.write(result1)
with open("result2.txt", "w", encoding="utf-8") as f:
    f.write(result2)
