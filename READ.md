# EPC Reasoning Engine

## Overview
EPC Reasoning Engine is an AI-powered system designed to analyze, retrieve, and reason over EPC (Engineering, Procurement, Construction) documents using Retrieval-Augmented Generation (RAG).

---

## Features
- Intelligent document ingestion and chunking
- FAISS-based semantic search
- AI-driven reasoning and summarization
- EPC domain-specific branch classification
- Evaluation metrics for retrieval quality

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Streamlit
- FAISS
- Sentence Transformers
- MySQL (Authentication)

---

##  Project Structure
```text
backend/
 ├── app/
 │   ├── api/
 │   ├── services/
 │   ├── core/
 │   └── main.py
streamlit_app/
 └── app.py

 How to Run
Backend
Bash
cd backend
uvicorn app.main:app --reload

Frontend
Bash
cd streamlit_app
streamlit run app.py

Evaluation Metrics
Retrieved Chunks Count
Context Utilization Score
Document Match Rate
Reasoning Mode Detection

 Future Enhancements
Clause conflict detection
Risk analysis heatmaps
Multi-document reasoning
Voice-based query interface