# services/embedding_service.py
from sentence_transformers import SentenceTransformer
from typing import List, Dict

# class EmbeddingService:
#     def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
#         self.model = SentenceTransformer(model_name)

#     def embed_texts(self, chunks: List[Dict]) -> List[Dict]:
#         """
#         Accepts a list of text chunks (with 'filename' and 'text') 
#         and returns a list with embeddings added.
#         """
#         texts = [chunk["text"] for chunk in chunks]
#         embeddings = self.model.encode(texts, show_progress_bar=True)

#         embedded_chunks = []
#         for chunk, vector in zip(chunks, embeddings):
#             embedded_chunks.append({
#                 "filename": chunk.get("filename"),
#                 "text": chunk.get("text"),
#                 "embedding": vector,
#                 "page": chunk.get("page")  # optional, if chunk has page info
#             })

#         return embedded_chunks
# services/embedding_service.py
class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, chunks:List[Dict]) -> List[Dict]:
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.model.encode(texts, show_progress_bar=True)

        embedded_chunks = []
        for chunk, vector in zip(chunks, embeddings):
            embedded_chunks.append({
                "filename": chunk.get("filename"),
                "text": chunk.get("text"),
                "embedding": vector,
                "page": chunk.get("page")  # optional
            })

        return embedded_chunks

    # ✅ Add this method
    def embed_query(self, text: str):
        """
        Embed a single query string.
        Returns a vector (list/array of floats).
        """
        return self.model.encode(text)