# Run this as a script (ingest.py)
from app.services.document_loader import DocumentLoader
from app.services.text_chunker import TextChunker
from app.services.embedding_service import EmbeddingService
from app.services.rag_pipeline import RAGPipeline
from app.core.config import VECTOR_DB_DIR, EMBEDDING_MODEL_NAME

# 1️⃣ Load PDFs
loader = DocumentLoader(docs_path="app/data/raw_docs")
docs = loader.load_documents()

# 2️⃣ Chunk PDFs
chunker = TextChunker()
chunks = chunker.chunk_documents(docs)

# 3️⃣ Generate embeddings
embed_service = EmbeddingService(model_name=EMBEDDING_MODEL_NAME)
embedded_chunks = embed_service.embed_texts(chunks)

# 4️⃣ Add to RAG pipeline & save FAISS
rag = RAGPipeline()
rag.ingest(chunks)

print("✅ Documents ingested and FAISS vector store ready!")
