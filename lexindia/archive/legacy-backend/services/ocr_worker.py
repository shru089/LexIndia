import pytesseract
from pdf2image import convert_from_bytes

class OCRWorker:
    """
    Processes court PDFs using OCR.
    """
    async def extract_text(self, pdf_bytes: bytes) -> str:
        # Converts PDF to images, then images to text
        images = convert_from_bytes(pdf_bytes)
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"
        return text

ocr_worker = OCRWorker()
