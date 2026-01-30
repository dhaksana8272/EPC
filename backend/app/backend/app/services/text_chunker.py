from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextChunker:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 150):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_documents(self, documents: list) -> list:
        chunks = []

        for doc in documents:
            split_texts = self.text_splitter.split_text(doc["text"])

            for chunk in split_texts:
                chunks.append({
                    "filename": doc["filename"],
                    "text": chunk
                })

        return chunks