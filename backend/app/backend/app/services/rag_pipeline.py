from app.services.vector_store import VectorStore
from app.services.llm_reasoner import LLMReasoner
from app.services.embedding_service import EmbeddingService
from app.services.branch_classifier import BranchClassifier
from app.services.summarizer import DocumentSummarizer
from app.services.reasoning import DocumentReasoner
from app.core.config import VECTOR_DB_DIR, TOP_K
from app.services.rag_metrics import RAGMetrics


class RAGPipeline:
    def __init__(self):
        # Core services
        self.embedder = EmbeddingService()
        self.llm = LLMReasoner()
        self.branch_classifier = BranchClassifier()

        # Specialized LLM tools
        self.summarizer = DocumentSummarizer()
        self.reasoner = DocumentReasoner(self.llm)

        # Vector store
        self.vector_store = VectorStore(dimension=384)
        self.vector_db_path = VECTOR_DB_DIR
        self.top_k = TOP_K

        # Load FAISS index
        try:
            self.vector_store.load(str(self.vector_db_path))
            print("✅ Vector store loaded from:", self.vector_db_path)
        except Exception as e:
            print("⚠️ No existing vector store found.", e)

    # ======================================================
    # INGEST
    # ======================================================
    def ingest(self, chunks: list):
        """
        chunks: List of dicts with keys: text, filename, page
        """
        embedded_chunks = self.embedder.embed_texts(chunks)
        self.vector_store.add_embeddings(embedded_chunks)
    
        self.vector_store.save(str(self.vector_db_path))
        print(f"✅ {len(chunks)} chunks ingested and indexed")

    # ======================================================
    # QUERY
    # ======================================================
    def query(self, question: str, document_name: str = None):
        q_lower = question.lower()
        detected_branch = self.branch_classifier.classify(question)

        # Embed query
        query_embedding = self.embedder.embed_query(question)

        # ==================================================
        # 🔥 SUMMARY MODE
        # ==================================================
        if "summarize" in q_lower or "summary" in q_lower:
            chunks = self.vector_store.search(
                query_embedding=query_embedding,
                top_k=60
            )

            if document_name:
                doc = document_name.lower()
                chunks = [
                    c for c in chunks
                    if doc in c.get("filename", "").lower()
                ]

            chunks = [
                c for c in chunks
                if c.get("text") and len(c["text"].strip()) > 50
            ]

            if not chunks:
                return {
                    "answer": "No sufficient content found in document.",
                    "branch": detected_branch,
                    "sources": [],
                    "confidence": 0.2
                }

            full_text = "\n".join(c["text"] for c in chunks)
            summary = self.summarizer.summarize(full_text)

            return {
                "answer": summary,
                "branch": detected_branch,
                "sources": [
                    {
                        "name": c.get("filename", "Unknown"),
                        "snippet": c["text"][:200]
                    }
                    for c in chunks[:5]
                ],
                "confidence": 0.9
            }

        # ==================================================
        # 🔍 RETRIEVAL + REASONING MODE
        # ==================================================
        retrieved_chunks = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=self.top_k
        )

        if document_name:
            doc = document_name.lower()
            retrieved_chunks = [
                c for c in retrieved_chunks
                if doc in c.get("filename", "").lower()
            ]

        retrieved_chunks = [
            c for c in retrieved_chunks
            if c.get("text") and len(c["text"].strip()) > 50
        ]

        if not retrieved_chunks:
            return {
                "answer": "Information not found in the document.",
                "branch": detected_branch,
                "sources": [],
                "confidence": 0.2
            }

        context = "\n".join(c["text"] for c in retrieved_chunks)
        
        # Reasoning vs direct QA
        if any(x in q_lower for x in ["why", "how", "impact", "implication", "effect"]):
            answer = self.reasoner.reason(question, context)
        else:
            answer = self.llm.generate_answer(question, context)

        confidence = min(0.95, 0.45 + 0.05 * len(retrieved_chunks))

        sources = [
            {
                "name": c.get("filename", "Unknown"),
                "snippet": c["text"][:200]
            }
            for c in retrieved_chunks[:5]
        ]
        seen = set()
        unique_sources = []

        for s in sources:
            key = (s["name"], s["snippet"][:50])
            if key not in seen:
                seen.add(key)
                unique_sources.append(s)
        sources = unique_sources
        # ===============================
        # 📊 RAG EVALUATION (TERMINAL ONLY)
        # ===============================
        RAGMetrics.print_metrics(
        retrieved_chunks=retrieved_chunks,
        context=context,
        answer=answer,
        document_name=document_name,
        reasoning_used=any(x in q_lower for x in ["why", "how", "impact", "implication", "effect"])
    )

        return {
            "answer": answer,
            "branch": detected_branch,
            "sources": sources,
            "confidence": round(confidence, 2)
        }