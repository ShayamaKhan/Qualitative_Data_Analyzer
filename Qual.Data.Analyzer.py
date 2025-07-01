import os
from tkinter import Tk, filedialog, simpledialog
import PyPDF2
import re
import pdfplumber

def select_pdfs():
    """Open a file dialog to select one or more PDF files."""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    return list(file_paths)

def get_keyword():
    """Prompt the user to enter a keyword."""
    root = Tk()
    root.withdraw()
    keyword = simpledialog.askstring("Keyword", "Enter the keyword to search for:")
    return keyword

def find_sentences_with_keyword(text, keyword):
    """Return all sentences containing the keyword as a paragraph."""
    # Split text into sentences (simple split by . ! ?)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Find sentences with the keyword (case-insensitive)
    matches = [s for s in sentences if keyword.lower() in s.lower()]
    # Join them as a paragraph
    return " ".join(matches)

def extract_text_pdfplumber(pdf_path):
    """Extract text from PDF using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def clean_sentence(sentence):
    # Remove extra spaces
    sentence = re.sub(r'\s+', ' ', sentence).strip()
    # Skip lines that look like references or DOIs
    if 'doi:' in sentence.lower():
        return None
    # Skip lines that are too short
    if len(sentence.split()) < 5:
        return None
    return sentence

def read_pdfs_and_find_keyword(pdf_paths, keyword):
    """Read each PDF and print cleaned sentences containing the keyword, one per line, with tone.
       Also, summarize the most common tone at the end."""
    tone_counts = {"Impact": 0, "No Impact": 0, "Conflicted": 0, "Uncertain": 0}
    for path in pdf_paths:
        print(f"\nSearching in: {os.path.basename(path)}")
        text = extract_text_pdfplumber(path)
        sentences = re.split(r'(?<=[.!?])\s+', text)
        matches = [s for s in sentences if keyword.lower() in s.lower()]
        cleaned = [clean_sentence(s) for s in matches]
        cleaned = [s for s in cleaned if s]  # Remove None values
        if cleaned:
            print(f"Sentences with '{keyword}':")
            for sentence in cleaned:
                tone = analyze_tone(sentence)
                tone_counts[tone] += 1
                print(f"{sentence}\nTone: {tone}\n")
        else:
            print(f"No sentences found with '{keyword}'.\n")
    # Print summary
    print("Tone summary:")
    for tone, count in tone_counts.items():
        print(f"{tone}: {count}")
    # Final thought
    most_common = max(tone_counts, key=tone_counts.get)
    print(f"\nFinal thought: The most common opinion is '{most_common}'.")

def analyze_tone(sentence):
    """Classify the sentence tone regarding sex and cybersickness."""
    s = sentence.lower()
    if any(phrase in s for phrase in [
        "no sex difference", "no effect of sex", "sex was not a factor", "sex differences were not found"
    ]):
        return "No Impact"
    if any(phrase in s for phrase in [
        "sex difference", "sex differences were found", "sex is a predictor", "sex has an impact"
    ]):
        return "Impact"
    if any(phrase in s for phrase in [
        "mixed results", "conflicting", "inconclusive", "unclear", "not clear"
    ]):
        return "Conflicted"
    return "Uncertain"

if __name__ == "__main__":
    pdf_files = select_pdfs()
    if pdf_files:
        keyword = get_keyword()
        if keyword:
            read_pdfs_and_find_keyword(pdf_files, keyword)
        else:
            print("No keyword entered.")
    else:
        print("No PDF files selected.")