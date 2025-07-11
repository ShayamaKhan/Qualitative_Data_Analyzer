import fitz  # pip install pymupdf


def extract_paragraphs_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    paragraphs = []

    for page in doc:
        text = page.get_text("text")
        lines = text.split('\n')
        paragraph = ""

        for line in lines:
            if line.strip() == "":
                if paragraph:
                    paragraphs.append(paragraph.strip())
                    paragraph = ""
            else:
                paragraph += " " + line.strip()

        if paragraph:
            paragraphs.append(paragraph.strip())

    return paragraphs


extracted_paragraphs = extract_paragraphs_from_pdf("Identifying Causes of and Solutions for Cybersickness in Immersive Technology Reformulation of a Research and Development Agenda.pdf")

with open("paragraphs1.txt", "w+", encoding="utf-8") as f:
    for paragraph in extracted_paragraphs:
        f.write(paragraph + "\n\n")

