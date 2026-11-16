import fitz
def extract_pdf_text(file_content: bytes) -> dict:
    try:
        pdf = fitz.open(stream=file_content, filetype="pdf")
        pages = []
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()
            pages.append({
                "page_no":page_number,
                "text":text
            })
        result = {
            "total_pages": len(pages),
            "title": pdf.metadata.get("title") or "Untitled Research Paper",
            "pages":pages
        }
        pdf.close()
        return result
    except Exception as error:
        raise ValueError(f"Unable to process PDF: {str(error)}")