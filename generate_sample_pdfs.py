import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_small_pdf(file_path):
    """Create a simple one-page PDF with a single line of text."""
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawString(100, 750, "This is a small test PDF.")
    c.save()

def create_multipage_pdf(file_path, num_pages=3):
    """Create a multi-page PDF with the same text on each page."""
    c = canvas.Canvas(file_path, pagesize=letter)
    for i in range(num_pages):
        c.drawString(100, 750, f"Page {i+1}: This is a multipage test PDF.")
        c.showPage()  # start a new page
    c.save()

def create_empty_pdf(file_path):
    """Create a PDF with a blank page."""
    c = canvas.Canvas(file_path, pagesize=letter)
    c.save()

def generate_sample_pdfs():
    # Define a folder for your sample PDFs
    sample_dir = os.path.join("tests", "samples")
    if not os.path.exists(sample_dir):
        os.makedirs(sample_dir)

    # Paths for the sample PDFs
    small_pdf = os.path.join(sample_dir, "sample_small.pdf")
    multipage_pdf = os.path.join(sample_dir, "sample_multipage.pdf")
    empty_pdf = os.path.join(sample_dir, "sample_empty.pdf")

    # Create the sample PDFs
    create_small_pdf(small_pdf)
    create_multipage_pdf(multipage_pdf, num_pages=5)
    create_empty_pdf(empty_pdf)

    print("Sample PDFs generated in:", sample_dir)

if __name__ == "__main__":
    generate_sample_pdfs()
