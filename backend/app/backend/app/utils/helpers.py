# utils/helpers.py
from app.services.document_loader import DocumentLoader
from app.services.text_chunker import TextChunker
from app.services.embedding_service import EmbeddingService
from app.services.rag_pipeline import RAGPipeline
from app.core.config import RAW_DOCS_DIR, VECTOR_DB_DIR, EMBEDDING_MODEL_NAME
import numpy as np

def load_and_chunk_documents(doc_path=RAW_DOCS_DIR, chunk_size=1000, chunk_overlap=150):
    """
    Load PDFs, chunk them, and return chunks
    """
    loader = DocumentLoader(doc_path)
    documents = loader.load_documents()

    chunker = TextChunker(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = chunker.chunk_documents(documents)
    return chunks


def embed_chunks(chunks, model_name=EMBEDDING_MODEL_NAME):
    """
    Embed the list of chunks using the embedding model
    """
    embed_service = EmbeddingService(model_name)
    embedded_chunks = embed_service.embed_texts(chunks)
    return embedded_chunks


def embed_query(query, model_name=EMBEDDING_MODEL_NAME):
    """
    Generate embedding for a query string
    """
    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(model_name)
    embedding = model.encode([query], show_progress_bar=False)[0]
    return np.array(embedding, dtype="float32")


def ingest_documents_to_rag(rag_pipeline: RAGPipeline, chunks):
    """
    Embed chunks and add them to the vector store in the RAG pipeline
    """
    embedded_chunks = embed_chunks(chunks)
    rag_pipeline.ingest(embedded_chunks)
    return len(embedded_chunks)
