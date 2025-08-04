# Qualitative Data Analyzer

> AI-powered tool for analyzing academic PDFs to extract and classify keyword-related content

## Overview

Qualitative Data Analyzer is a desktop application that uses artificial intelligence to analyze academic PDFs for specific keywords and factors. The tool automatically extracts relevant paragraphs, determines their tone regarding your keywords, and generates comprehensive Excel reports.

### What It Does
- **Extracts text** from academic PDF documents
- **Finds relevant paragraphs** containing your specified keywords
- **Uses AI** to classify the tone of each paragraph (Supportive, Neutral, Opposing)
- **Generates Excel reports** with detailed analysis and scoring
- **Perfect for** literature reviews, research analysis, and academic studies

### Sample Output
The tool creates an Excel file with:
- Keyword analysis for each term you specify
- Extracted paragraphs containing those keywords
- AI-powered tone classification with explanations
- Scoring system and cumulative analysis
- Overall tone summary for each keyword

## Prerequisites

Before you start, you'll need:

1. **Python 3.8 or newer** installed on your computer
   - Download from [python.org](https://www.python.org/downloads/)
   - Make sure to check "Add Python to PATH" during installation

2. **OpenAI API Key** (required for AI analysis)
   - Sign up at [OpenAI Platform](https://platform.openai.com/)
   - Go to [API Keys](https://platform.openai.com/api-keys) in your dashboard
   - Create a new secret key and copy it
   - **Important**: You'll need billing set up with OpenAI (usually costs $1-5 per analysis)

## Installation & Setup

### Step 1: Get the Project Files
Clone or download this repository to your computer. You should have a folder with these files:
```
Qualitative_Data_Analyzer/
├── main.py
├── keys.py.template.py
├── requirements.txt
├── README.md
└── DEVELOPER_GUIDE.md
```

### Step 2: Install Required Packages
Open a terminal/command prompt in your project folder and run:

**Windows:**
```bash
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
pip3 install -r requirements.txt
```

### Step 3: Set Up Your API Key

1. **Copy the template file:**
   - Find `keys.py.template.py` in your project folder
   - Copy it and rename the copy to `keys.py`

2. **Add your API key:**
   Open `keys.py` in any text editor and replace the placeholder:
   
   ```python
   # OpenAI API Key
   # Get your API key from: https://platform.openai.com/api-keys
   open_ai_api_key = "sk-proj-your-actual-api-key-here"
   ```

⚠️ **Security Note**: Never share your API key or commit the `keys.py` file to GitHub!


## How to Use

### Step 1: Prepare Your PDF
- Make sure your PDF contains searchable text (not just scanned images)
- The PDF should be in English

### Step 2: Launch the Application
Run `python main.py`  

<img width="795" height="208" alt="Analysis running" src="https://github.com/user-attachments/assets/bd012732-248a-4263-9bc0-27eaf74abf6a" />  

When successful, you should see a window like this:  

<img width="589" height="177" alt="Application GUI" src="https://github.com/user-attachments/assets/de96cc79-5d02-4219-b199-4753a133dfd5" />

### Step 3: Select Your PDF File and Enter Your Keywords
1. Click the **"Browse"** button
2. Navigate to your PDF file and select it
3. The file path will appear in the text field
4. In the "Keywords" field, enter the terms you want to analyze
5. **Separate multiple keywords with commas**  
Examples:
   - `cybersickness, motion sickness, VR`
   - `gender, age, latency`
   - `virtual reality, augmented reality, mixed reality`

<img width="595" height="176" alt="File selection interface" src="https://github.com/user-attachments/assets/fa6a73ce-7938-4f34-b723-73e6c3dcaa40" />

### Step 4: Run the Analysis
1. Click **"Run Analysis"**
2. Processing time depends on PDF size (typically 1-5 minutes)
3. You'll see a success message when complete

<img width="545" height="222" alt="image" src="https://github.com/user-attachments/assets/eb7f2e59-723e-497f-874e-a430e927f094" />

### Step 5: View Your Results
1. Look for `factor_analysis_results.xlsx` in your project folder
2. Open it with Excel 
3. Review the analysis for each keyword

<img width="806" height="251" alt="Excel results" src="https://github.com/user-attachments/assets/7560e7a2-ed8e-42f6-9d4a-2b49f422440d" />

## Understanding Your Results

The Excel file contains these columns:

| Column | Description |
|--------|-------------|
| **Keyword** | The search term you specified |
| **Paragraph #** | Sequential numbering of relevant paragraphs |
| **Extracted Text** | The actual paragraph text from the PDF |
| **Tone** | AI classification: Supportive, Neutral, or Opposing |
| **Explanation** | AI's reasoning for the tone classification |
| **Score** | Numeric value: Supportive=+1, Neutral=0, Opposing=-1 |
| **Cumulative Score** | Running total of scores for the keyword |
| **Overall Tone** | Summary tone for all paragraphs of this keyword |

### Tone Classifications:
- **Supportive**: The paragraph affirms or supports the keyword's effect/relationship
- **Neutral**: The paragraph mentions the keyword without taking a stance  
- **Opposing**: The paragraph indicates no effect or contradictory evidence
- **Not Discussed**: The keyword was not found in the document

## Common Issues & Solutions

### "Error: Please provide all inputs"
**Problem**: Missing PDF file or keywords  
**Solution**: Make sure both the PDF file and keywords fields are filled

### "API Error" or "Invalid API Key"
**Problem**: Issue with your OpenAI API key  
**Solutions**:
- Check that your API key is correctly copied in `keys.py`
- Verify your OpenAI account has billing set up
- Make sure your API key hasn't expired

### "Cannot overwrite Excel file"
**Problem**: The results file is open in Excel  
**Solution**: Close `factor_analysis_results.xlsx` before running a new analysis

### "No text extracted from PDF"
**Problem**: PDF contains only images or is password-protected  
**Solutions**:
- Try a different PDF with searchable text
- Remove password protection from the PDF
- Use OCR software to convert image-based PDFs to text

### Application freezes or takes too long
**Problem**: Large PDF or many keywords  
**Solutions**:
- Try with a smaller PDF first
- Reduce the number of keywords
- Be patient - complex analysis can take several minutes
- Check your internet connection (required for AI processing)

## Limitations & Notes

### Current Limitations:
- **English only**: Works best with English-language PDFs
- **Internet required**: Needs connection for AI processing  
- **API costs**: Each analysis uses OpenAI credits 
- **Processing time**: Large PDFs may take 5-10 minutes
- **Text-based PDFs only**: Cannot analyze image-only or scanned documents

### Best Practices:
- Test with a small PDF first
- Use specific, relevant keywords
- Close Excel files before running new analysis
- Keep your API key secure and private

## Example Use Cases

### Academic Research
- **Literature Review**: Analyze multiple papers for sentiment toward specific concepts
- **Systematic Review**: Classify studies as supporting/opposing a hypothesis
- **Meta-Analysis Prep**: Extract and categorize relevant findings

### Content Analysis
- **Policy Documents**: Analyze stance on specific topics
- **Survey Reports**: Extract sentiment about particular issues
- **Technical Papers**: Classify discussions around methodologies or technologies

## Getting Help

### For Technical Issues:
1. Check the [Troubleshooting](#common-issues--solutions) section above
2. Review the [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for technical details
3. Create an issue on this GitHub repository

### For Development:
- See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md) for code documentation
- Contributions welcome via pull requests

 
