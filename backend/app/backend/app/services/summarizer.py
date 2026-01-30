from transformers import pipeline


class DocumentSummarizer:
    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn"
        )

    def summarize(self, text: str) -> str:
        if not text or len(text.strip()) < 200:
            return "Not enough content available to generate a summary."

        result = self.summarizer(
            text[:4000],
            max_length=300,
            min_length=120,
            do_sample=False
        )

        return result[0]["summary_text"]