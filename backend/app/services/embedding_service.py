from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, chunks: list) -> list:
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)

        embedded_chunks = []
        for chunk, vector in zip(chunks, embeddings):
            embedded_chunks.append({
                "filename": chunk["filename"],
                "text": chunk["text"],
                "embedding": vector
            })

        return embedded_chunks