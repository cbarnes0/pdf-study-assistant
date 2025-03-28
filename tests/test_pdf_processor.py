import unittest
import os
from backend.pdf_processor import extract_text_from_pdf

class TestPDFProcessor(unittest.TestCase):
    def test_extract_text_small_pdf(self):
        # Test a simple, one-page PDF with some text.
        test_pdf_path = os.path.join("tests", "samples", "sample_small.pdf")
        self.assertTrue(os.path.exists(test_pdf_path), "Test small PDF file does not exist.")
        
        try:
            chunks = extract_text_from_pdf(test_pdf_path, chunk_size=500)
            # Expect at least one non-empty chunk.
            self.assertIsInstance(chunks, list)
            self.assertGreater(len(chunks), 0)
            for chunk in chunks:
                self.assertIsInstance(chunk, str)
                self.assertTrue(len(chunk) > 0)
        except Exception as e:
            self.fail(f"PDF extraction for small PDF failed with exception: {e}")
    
    def test_extract_text_multipage_pdf(self):
        # Test a multipage PDF to ensure extraction spans multiple pages.
        test_pdf_path = os.path.join("tests", "samples", "sample_multipage.pdf")
        self.assertTrue(os.path.exists(test_pdf_path), "Test multipage PDF file does not exist.")
        
        try:
            chunks = extract_text_from_pdf(test_pdf_path, chunk_size=500)
            self.assertIsInstance(chunks, list)
            # For a multipage PDF, we expect multiple chunks or a larger text
            self.assertGreaterEqual(len(chunks), 1)
            for chunk in chunks:
                self.assertIsInstance(chunk, str)
                self.assertTrue(len(chunk) > 0)
        except Exception as e:
            self.fail(f"PDF extraction for multipage PDF failed with exception: {e}")

    def test_extract_text_empty_pdf(self):
        # Test an empty PDF, which may return an empty string or a list with an empty string.
        test_pdf_path = os.path.join("tests", "samples", "sample_empty.pdf")
        self.assertTrue(os.path.exists(test_pdf_path), "Test empty PDF file does not exist.")
        
        try:
            chunks = extract_text_from_pdf(test_pdf_path, chunk_size=500)
            self.assertIsInstance(chunks, list)
            # Depending on your implementation, an empty PDF might return a list with an empty string.
            # Here we assume that behavior; adjust the assertions if your function should behave differently.
            self.assertEqual(len(chunks), 1)
            self.assertEqual(chunks[0], "")
        except Exception as e:
            self.fail(f"PDF extraction for empty PDF failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
