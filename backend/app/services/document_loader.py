from pathlib import Path
import pdfplumber

class DocumentLoader:
    def __init__(self, docs_path: str):
        self.docs_path = Path(docs_path)

    def load_documents(self) -> list:
        documents = []

        for pdf_file in self.docs_path.glob("*.pdf"):
            with pdfplumber.open(pdf_file) as pdf:
                full_text = ""
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"

                documents.append({
                    "filename": pdf_file.name,
                    "text": full_text
                })

        return documents