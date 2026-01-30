# services/vector_store.py
import faiss
import numpy as np
import pickle
from pathlib import Path

class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add_embeddings(self, embedded_chunks: list):
        if not embedded_chunks:
            return

        vectors = np.array(
            [chunk["embedding"] for chunk in embedded_chunks],
            dtype="float32"
        )
        self.index.add(vectors)
        self.metadata.extend(embedded_chunks)

    def save(self, path: str):
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)

        # ✅ FAISS NEEDS STRING PATH
        faiss.write_index(self.index, str(path / "index.faiss"))

        with open(path / "metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

        print("💾 Vector store saved successfully")

    def load(self, path: str):
        path = Path(path)

        index_path = path / "index.faiss"
        meta_path = path / "metadata.pkl"

        if not index_path.exists() or not meta_path.exists():
            raise FileNotFoundError(f"No FAISS index found in {path}")

        # ✅ STRING PATH AGAIN
        self.index = faiss.read_index(str(index_path))

        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)

        print("✅ Vector store loaded successfully")

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> list:
        if self.index.ntotal == 0:
            return []

        query_vector = np.array([query_embedding], dtype="float32")
        distances, indices = self.index.search(query_vector, top_k)

        return [
            self.metadata[idx]
            for idx in indices[0]
            if idx < len(self.metadata)
        ]
