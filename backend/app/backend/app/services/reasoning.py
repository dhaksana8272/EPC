class DocumentReasoner:
    def __init__(self, llm):
        self.llm = llm

    def reason(self, question: str, context: str) -> str:
        prompt = f"""
You are a contract analysis assistant.

Answer the question ONLY using the provided document content.
If the answer is not explicitly present, say:
"Information not found in the document."

If the document does not explicitly mention the concept,
explain the closest relevant clauses and clearly state the limitation.
Do not invent clauses.

DOCUMENT:
{context}

QUESTION:
{question}

ANSWER:
"""
        return self.llm.generate_answer(
            question=question,
            context=prompt
        )