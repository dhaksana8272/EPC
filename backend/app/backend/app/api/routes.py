# backend/app/api/routes.py

from fastapi import APIRouter, HTTPException
from app.schemas.request import EPCQueryRequest
from app.schemas.response import EPCQueryResponse
from app.services.rag_pipeline import RAGPipeline
from app.core.logger import get_logger
from pathlib import Path

logger = get_logger("API_ROUTER")

router = APIRouter(tags=["EPC Query"])


# ---- RAG configuration ----
EMBEDDING_DIM = 384  # all-MiniLM-L6-v2
VECTOR_DB_PATH = Path("backend/app/vector_db")  # same path used in ingest

# Initialize RAG pipeline once (singleton)
rag_pipeline = RAGPipeline()
    # embedding_dim=EMBEDDING_DIM,
    # vector_db_path=VECTOR_DB_PATH



@router.post("/query", response_model=EPCQueryResponse)
async def query_epc(request: EPCQueryRequest):
    """
    POST /api/query
    Process EPC-related queries using RAG pipeline
    """
    logger.info(f"Received query request: {request.model_dump()}")

    try:
        response = rag_pipeline.query(
            request.query,
            # request.branch,
            # request.document_name
        )
        logger.info("Query processed successfully")
        return response

    except Exception as e:
        logger.exception("Error while processing EPC query")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
