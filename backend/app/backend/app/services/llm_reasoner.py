# services/llm_reasoner.py
from llama_cpp import Llama

class LLMReasoner:
    def __init__(self):
        self.llm = Llama(
            model_path="models/Phi-3-mini-4k-instruct-q4.gguf",
            n_ctx=2048,
            n_threads=8,        # adjust to your CPU cores
            n_gpu_layers=0,     # CPU only
            verbose=False
        )

    def generate_answer(self, question: str, context: str, max_new_tokens: int = 200) -> str:
        prompt = f"""Context:
{context}

Question:
{question}

Answer:"""

        output = self.llm(
            prompt,
            max_tokens=max_new_tokens,
            temperature=0.1,
            stop=["Question:", "Context:"]
        )

        return output["choices"][0]["text"].strip()
