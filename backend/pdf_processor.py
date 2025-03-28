import logging
from pypdf import PdfReader

# Set up logging for this module
logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path, chunk_size=1000):
    """
    Extract text from a PDF and split it into chunks of roughly 'chunk_size' characters.
    Returns a list of text chunks.
    """
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            full_text = ""
            for page in reader.pages:
                page_text = page.extract_text() or ""
                full_text += page_text + "\n"
    except Exception as e:
        logger.error(f"Error reading PDF file {pdf_path}", exc_info=True)
        raise Exception(f"Failed to process PDF: {e}")

    # Optional: if the text is very long, split it into chunks
    if len(full_text) <= chunk_size:
        return [full_text.strip()]
    else:
        chunks = []
        start = 0
        while start < len(full_text):
            chunk = full_text[start:start + chunk_size]
            chunks.append(chunk.strip())
            start += chunk_size
        return chunks
