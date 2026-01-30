# services/document_loader.py
from pathlib import Path
import pdfplumber
from app.core.config import RAW_DOCS_DIR

class DocumentLoader:
    def __init__(self, docs_path: str = None):
        # Default to RAW_DOCS_DIR from config
        self.docs_path = Path(docs_path) if docs_path else RAW_DOCS_DIR

    def load_documents(self) -> list:
        """
        Loads all PDF documents in the docs_path directory.
        Returns a list of dictionaries: {"filename": str, "text": str}
        """
        documents = []

        for pdf_file in self.docs_path.glob("*.pdf"):
            try:
                with pdfplumber.open(pdf_file) as pdf:
                    full_text = ""
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            full_text += text + "\n"

                # Skip empty documents
                if full_text.strip():
                    documents.append({
                        "filename": pdf_file.name,
                        "text": full_text
                    })

            except Exception as e:
                print(f"Error loading {pdf_file.name}: {e}")

        return documents
