# test_rag_pipeline.py

from services.rag_pipeline import RAGPipeline


rag = RAGPipeline()

# Step 1: Ingest documents (only once)
documents = [
    "EPC projects involve engineering, procurement, and construction phases.",
    "Procurement includes vendor selection, contracts, and logistics.",
    "Construction phase focuses on execution, safety, and quality control."
]

rag.ingest_documents(documents)

# Step 2: Ask a real question
query = "What are the key phases of an EPC project?"
answer = rag.answer(query)

print("QUERY:", query)
print("\nANSWER:\n", answer)
