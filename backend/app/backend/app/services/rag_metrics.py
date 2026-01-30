# services/rag_metrics.py
import re

class RAGMetrics:
    @staticmethod
    def token_overlap_ratio(answer: str, context: str) -> float:
        a_tokens = set(re.findall(r"\w+", answer.lower()))
        c_tokens = set(re.findall(r"\w+", context.lower()))

        if not a_tokens:
            return 0.0

        return round(len(a_tokens & c_tokens) / len(a_tokens), 3)

    @staticmethod
    def print_metrics(
        retrieved_chunks: list,
        context: str,
        answer: str,
        document_name: str = None,
        reasoning_used: bool = False
    ):
        total = len(retrieved_chunks)
        valid = len([c for c in retrieved_chunks if len(c.get("text", "")) > 50])

        doc_hits = 0
        if document_name:
            doc = document_name.lower().replace(".pdf", "").strip()
            doc_hits = sum(
                1 for c in retrieved_chunks
                if doc and doc in c.get("filename", "").lower()
    )

                  

        overlap = RAGMetrics.token_overlap_ratio(answer, context)

        print("\n📊 RAG EVALUATION METRICS")
        print("-" * 40)
        print(f"🔹 Retrieved Chunks       : {total}")
        print(f"🔹 Valid Chunks (>50 chars): {valid}")
        print(f"🔹 Document Match Rate    : {doc_hits}/{total}")
        print(f"🔹 Avg Chunk Length       : {sum(len(c['text']) for c in retrieved_chunks) // max(1, total)}")
        print(f"🔹 Context Utilization    : {overlap}")
        print(f"🔹 Reasoning Mode         : {'ON' if reasoning_used else 'OFF'}")
        print("-" * 40)