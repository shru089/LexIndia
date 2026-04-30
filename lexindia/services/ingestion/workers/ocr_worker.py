import pytesseract
from pdf2image import convert_from_bytes
from typing import str

class OCRWorker:
    """
    Handles OCR processing for scanned court judgments.
    Uses Tesseract + pdf2image.
    """
    
    async def process_pdf(self, pdf_bytes: bytes) -> str:
        """
        Converts PDF pages to images and runs OCR to extract text.
        """
        images = convert_from_bytes(pdf_bytes)
        full_text = ""
        for image in images:
            text = pytesseract.image_to_string(image)
            full_text += text + "\n"
        
        return full_text

ocr_worker = OCRWorker()
