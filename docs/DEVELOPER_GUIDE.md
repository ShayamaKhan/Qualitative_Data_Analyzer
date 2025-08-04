# Qualitative Data Analyzer - Developer Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Setup for Development](#setup-for-development)
4. [Code Structure](#code-structure)
5. [Core Functions](#core-functions)
6. [API Integration](#api-integration)
7. [Configuration Management](#configuration-management)
8. [Testing](#testing)
9. [Contributing](#contributing)
10. [Troubleshooting](#troubleshooting)

## Project Overview

The Qualitative Data Analyzer is a Python-based desktop application that uses AI to analyze academic PDFs for specific keywords and factors. It leverages OpenAI's GPT models to extract paragraphs, classify tones, and generate comprehensive analysis reports.

### Key Features
- PDF text extraction using PyMuPDF
- AI-powered paragraph segmentation
- Tone classification (Supportive, Neutral, Opposing)
- Excel report generation with formatting
- Tkinter-based GUI interface

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   GUI Layer     │    │  Analysis Core  │    │  Output Layer   │
│   (Tkinter)     │───▶│   (OpenAI API)  │───▶│   (Excel)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                       │                       │
        │                       │                       │
   ┌─────────┐          ┌─────────────┐         ┌─────────────┐
   │File I/O │          │PDF Analysis │         │Data Storage │
   │ Dialog  │          │ Processing  │         │& Formatting │
   └─────────┘          └─────────────┘         └─────────────┘
```

## Setup for Development

### Prerequisites
- Python 3.8 or higher
- Git (for version control)
- Code editor (VS Code recommended)

### Development Environment Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShayamaKhan/Qualitative_Data_Analyzer.git
   cd Qualitative_Data_Analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys**
   ```bash
   copy keys.py.template.py keys.py
   # Edit keys.py with your OpenAI API key
   ```

5. **Verify installation**
   ```bash
   python main.py
   ```

## Code Structure

```
Qualitative_Data_Analyzer/
├── main.py                 # Main application entry point
├── keys.py.template.py     # Template for API keys
├── requirements.txt        # Python dependencies
├── README.md              # User guide
├── DEVELOPER_GUIDE.md     # This file
├── LICENSE                # Project license
└── __pycache__/          # Python cache files
```

### Main Components

#### `main.py`
The core application file containing:
- **Paragraph extraction logic** (`extract_paragraphs()`)
- **Tone classification** (`classify_tone()`)
- **Analysis workflow** (`run_analysis()`)
- **Excel output generation** (`save_to_excel()`)
- **GUI implementation** (Tkinter interface)

## Core Functions

### 1. Paragraph Extraction
```python
def extract_paragraphs(text, client):
    """
    Uses OpenAI API to intelligently split text into paragraphs.
    
    Args:
        text (str): Raw text from PDF
        client (OpenAI): OpenAI client instance
    
    Returns:
        list: List of extracted paragraphs
    """
```

**Implementation Details:**
- Uses streaming API for real-time processing
- Employs `<P>` markers for paragraph separation
- Temperature set to 0 for consistent results

### 2. Tone Classification
```python
def classify_tone(paragraph, keyword, client):
    """
    Classifies the tone of a paragraph regarding a specific keyword.
    
    Args:
        paragraph (str): Text to analyze
        keyword (str): Target keyword
        client (OpenAI): OpenAI client instance
    
    Returns:
        str: Tone classification with explanation
    """
```

**Classification Categories:**
- **Supportive**: Affirms or supports the keyword's effect/relationship
- **Neutral**: Mentions keyword without taking a stance
- **Opposing**: Indicates no effect or contradictory evidence

### 3. Analysis Workflow
```python
def run_analysis(pdf_path, keywords):
    """
    The main analysis pipeline that processes PDF and generates results.
    
    Args:
        pdf_path (str): Path to input PDF file
        Keywords (list): List of keywords to analyze
    """
```

**Process Flow:**
1. Extract text from PDF using PyMuPDF
2. Split text into paragraphs using AI
3. Filter paragraphs containing keywords
4. Classify the tone for each relevant paragraph
5. Calculate scores and cumulative metrics
6. Generate formatted Excel output

### 4. Excel Output Generation
```python
def save_to_excel(excel_rows, output_excel, row_ranges):
    """
    Creates a formatted Excel file with analysis results.
    
    Args:
        excel_rows (list): Data rows for Excel
        output_excel (str): Output file path
        row_ranges (list): Row ranges for each keyword
    """
```

**Excel Features:**
- Styled headers with a blue background
- Bordered cells for better readability
- Automatic column width adjustment
- Conditional formatting for different tones

## API Integration

### OpenAI Configuration
The application uses two OpenAI models:
- **gpt-4o-mini**: For paragraph extraction (streaming)
- **gpt-4o**: For tone classification (single response)

### API Key Management
```python
from keys import open_ai_api_key
client = OpenAI(api_key=open_ai_api_key)
```

**Security Best Practices:**
- API keys stored in a separate `keys.py` file
- `keys.py` added to `.gitignore`
- Template file provided for easy setup

### Error Handling
```python
try:
    response = client.chat.completions.create(...)
except Exception as e:
    messagebox.showerror("Error", str(e))
```

## Configuration Management

### Dependencies (`requirements.txt`)
```
pymupdf      # PDF processing
pandas       # Data manipulation
openpyxl     # Excel file generation
openai       # OpenAI API client
```

### API Key Template (`keys.py.template.py`)
```python
# Template file for API keys
open_ai_api_key = "your_openai_api_key_here"
```

**Setup Instructions:**
1. Copy template to `keys.py`
2. Replace the placeholder with the actual API key
3. Ensure `keys.py` is in `.gitignore`

## Testing

### Manual Testing Checklist
- [ ] GUI launches without errors
- [ ] PDF file selection works
- [ ] Keyword input validation
- [ ] Analysis completes successfully
- [ ] Excel file generates correctly
- [ ] Error handling for invalid inputs

### Test Cases
1. **Valid PDF with keywords**: Should generate complete analysis
2. **PDF without keywords**: Should show "Not Discussed" entries
3. **Invalid PDF**: Should show appropriate error message
4. **Empty keywords**: Should prompt for input
5. **Large PDF**: Should handle processing time gracefully

### Sample Test Data
```python
# Test keywords for academic papers
test_keywords = ["cybersickness", "motion sickness", "virtual reality", "VR"]

# Expected output structure
expected_columns = [
    "Keyword", "Paragraph Number", "Extracted Paragraph", 
    "Tone", "Explanation", "Score", "Cumulative Score", "Overall Tone"
]
```

## Contributing

### Code Style Guidelines
- Follow PEP 8 for Python code formatting
- Use descriptive variable names
- Add docstrings for all functions
- Keep functions focused and modular

### Git Workflow
1. Create feature branch: `git checkout -b feature/new-feature`
2. Make changes and test thoroughly
3. Commit with descriptive messages: `git commit -m "Add: new feature description"`
4. Push branch: `git push origin feature/new-feature`
5. Create a pull request for review

### Commit Message Format
```
Type: Brief description

Detailed explanation of changes (if needed)

- Add new feature X
- Fix bug in Y
- Update documentation for Z
```

**Types:**
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Modification to existing feature
- `Remove:` Deletion of code/feature
- `Docs:` Documentation changes

### Adding New Features

#### Example: Adding New Classification Categories
1. Update `classify_tone()` function prompt
2. Modify the tone scoring system in `run_analysis()`
3. Update Excel formatting if needed
4. Test with various input scenarios
5. Update documentation

```python
# New tone categories example
tone_score = {
    "Supportive": 1, 
    "Neutral": 0, 
    "Opposing": -1,
    "Mixed": 0.5,      # New category
    "Unclear": 0       # New category
}
```

## Troubleshooting

### Common Issues

#### 1. OpenAI API Errors
**Problem**: API key invalid or quota exceeded
**Solution**: 
- Verify API key in `keys.py`
- Check OpenAI account billing status
- Ensure the API key has the correct permissions

#### 2. PDF Processing Errors
**Problem**: Cannot extract text from PDF
**Solution**:
- Verify PDF is not password-protected
- Check if PDF contains searchable text (not just images)
- Try with different PDF files

#### 3. Excel File Locked
**Problem**: Cannot save Excel file
**Solution**:
- Close the Excel file if open
- Check file permissions
- Verify the output directory is writable

#### 4. GUI Not Responding
**Problem**: Interface freezes during analysis
**Solution**:
- Large PDFs take time to process
- Consider adding a progress bar for user feedback
- Check system resources

### Debug Mode
Add debug prints for troubleshooting:

```python
def run_analysis(pdf_path, keywords):
    print(f"Starting analysis for: {pdf_path}")
    print(f"Keywords: {keywords}")
    
    # ... existing code ...
    
    print(f"Extracted {len(all_paragraphs)} paragraphs")
    print(f"Processing {len(keyword_paragraphs)} relevant paragraphs for '{keyword}'")
```

### Performance Optimization
- **Large PDFs**: Consider processing pages in batches
- **Multiple keywords**: Implement parallel processing
- **API calls**: Add retry logic for network issues

### Error Logging
Consider adding logging for production use:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='analyzer.log'
)
```

## Future Enhancements

### Planned Features
- [ ] Support for multiple PDF files
- [ ] Custom tone categories
- [ ] Progress bar for long operations
- [ ] Export to different formats (CSV, JSON)
- [ ] Batch processing capabilities
- [ ] Advanced filtering options

### Architecture Improvements
- [ ] Separate GUI from analysis logic
- [ ] Add configuration file support
- [ ] Implement plugin system for new analyzers
- [ ] Add unit tests
- [ ] Create web-based interface option

## Support

For development questions or issues:
1. Check this developer guide
2. Review existing code comments
3. Test with sample PDFs
4. Create GitHub issue with detailed description

