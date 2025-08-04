# Qualitative Data Analyzer – User Guide

## Overview

Qualitative Data Analyzer is a desktop tool that uses AI to analyze academic PDFs for specific keywords and factors. It extracts relevant paragraphs, determines the tone, and saves the results in an Excel file.

## How It Works?
The tool extracts paragraphs from your selected PDF.
For each keyword you enter, it finds relevant paragraphs.
It uses AI to classify the tone of each paragraph for each keyword (Supportive, Neutral, Opposing).
Results are saved in an Excel file with columns for keyword, paragraph number, extracted text, tone, explanation, score, cumulative score, and overall tone.

## Requirements

- Python 3.8 or newer
- Python packages:
pymupdf, 
pandas, 
openpyxl, 
openai

- OpenAI API key


## How to run?

1. **Install Python packages**  

2. **Set up your OpenAI API key**  
You can get your API key by signing up at [OpenAI](https://platform.openai.com/) and creating a new key in your account dashboard.
Never share your API key publicly.

4. **Start the application**  
Use the main.py file
<img width="795" height="208" alt="image" src="https://github.com/user-attachments/assets/bd012732-248a-4263-9bc0-27eaf74abf6a" />


6. **Use the graphical window**
<img width="589" height="177" alt="image" src="https://github.com/user-attachments/assets/de96cc79-5d02-4219-b199-4753a133dfd5" />
<img width="595" height="176" alt="image" src="https://github.com/user-attachments/assets/fa6a73ce-7938-4f34-b723-73e6c3dcaa40" />


Click Browse to select your PDF file.  
Enter keywords (comma-separated, e.g. gender, age, latency).  
Click Run Analysis.

5. **View results**
<img width="539" height="227" alt="image" src="https://github.com/user-attachments/assets/d39d55ae-c555-4ec1-b8bc-4d09d7539c34" />
<img width="806" height="251" alt="image" src="https://github.com/user-attachments/assets/7560e7a2-ed8e-42f6-9d4a-2b49f422440d" />

Results are saved in factor_analysis_results.xlsx in your project folder.  
Open this file in Excel to view the analysis.

## Troubleshooting
1. Excel file won’t update: Close factor_analysis_results.xlsx before running the analysis.
2. API errors: Check your API key in keys.py.
 
