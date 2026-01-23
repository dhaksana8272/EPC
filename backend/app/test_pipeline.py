from services.document_loader import DocumentLoader
from services.text_chunker import TextChunker
from services.embedding_service import EmbeddingService
from services.vector_store import VectorStore
from services.branch_classifier import BranchClassifier

# 1. Load documents
loader = DocumentLoader("data/raw_docs")
documents = loader.load_documents()
print(f"Loaded {len(documents)} documents")

# 2. Chunk documents
chunker = TextChunker()
chunks = chunker.chunk_documents(documents)
print(f"Created {len(chunks)} chunks")

# 3. Create embeddings
embedder = EmbeddingService()
embedded_chunks = embedder.embed_texts(chunks)
print(f"Embedded {len(embedded_chunks)} chunks")

# 4. Store in FAISS
dimension = len(embedded_chunks[0]["embedding"])
vector_store = VectorStore(dimension)
vector_store.add_embeddings(embedded_chunks)
print("FAISS index created")

# 5. Test search
query_text = "concrete foundation and structural slab"
query_embedding = embedder.model.encode(query_text)
results = vector_store.search(query_embedding)

print("Search results:")
for r in results:
    print("-", r["filename"])

# 6. Test branch classification
classifier = BranchClassifier()
branch = classifier.classify(query_text)
print("Predicted branch:", branch)