import faiss
import numpy as np
import os
import pickle

class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add_embeddings(self, embedded_chunks: list):
        vectors = np.array(
            [chunk["embedding"] for chunk in embedded_chunks]
        ).astype("float32")

        self.index.add(vectors)
        self.metadata.extend(embedded_chunks)

    def save(self, path: str):
        os.makedirs(path, exist_ok=True)
        faiss.write_index(self.index, os.path.join(path, "index.faiss"))

        with open(os.path.join(path, "metadata.pkl"), "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, path: str):
        self.index = faiss.read_index(os.path.join(path, "index.faiss"))

        with open(os.path.join(path, "metadata.pkl"), "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query_embedding, top_k: int = 5) -> list:
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results