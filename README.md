# Qualitative Data Analyzer – User Guide

## Overview

Qualitative Data Analyzer is a desktop tool that uses AI to analyze academic PDFs for specific keywords and factors. It extracts relevant paragraphs, determines the tone, and saves the results in an Excel file.

## How It Works
    The tool extracts paragraphs from your selected PDF.
    For each keyword you enter, it finds relevant paragraphs.
    It uses AI to classify the tone of each paragraph for each keyword (Supportive, Neutral, Opposing).
    Results are saved in an Excel file with columns for keyword, paragraph number, extracted text, tone, explanation, score, cumulative score, and overall tone.

## Requirements

- Python 3.8 or newer
- The following Python packages:
  - pymupdf
  - pandas
  - openpyxl
  - openai
- OpenAI API key


## How to run

1. **Install Python packages**  
   Open a terminal in your project folder and run:
   ```sh
   pip install pymupdf pandas openpyxl openai

2. **Set up your OpenAI API key**  
   Set up your OpenAI API key
Copy keys.py.template to keys.py.
Edit keys.py and add your API key

3. **Start the application**
    python main.py

4. **Use the graphical window**
    Click Browse to select your PDF file.
    Enter keywords (comma separated, e.g. gender, age, latency).
    Click Run Analysis.

5.**View results**
        Results are saved in factor_analysis_results.xlsx in your project folder.open this file in Excel to view the analysis.

## Troubleshooting
1. Excel file won’t update: Close factor_analysis_results.xlsx before running the analysis.
2. API errors:Check your API key in keys.py.
 