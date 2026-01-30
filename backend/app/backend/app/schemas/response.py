from pydantic import BaseModel, Field
from typing import List, Optional

class SourceDocument(BaseModel):
    """
    Represents a single source document used by RAG to answer the query.
    """
    name: str = Field(..., description="Filename of the EPC document used as reference")
    page: Optional[int] = Field(None, description="Page number of the reference")
    snippet: Optional[str] = Field(None, description="Text snippet from the document used in answer")


class EPCQueryResponse(BaseModel):
    """
    Response schema for EPC Reasoning Engine.
    - Provides LLM-generated answer
    - Includes branch info and source documents (RAG)
    - Optional metadata (confidence score)
    """
    answer: str = Field(..., description="LLM-generated answer to the user query")
    branch: Optional[str] = Field(None, description="Detected EPC branch, if any")
    sources: List[SourceDocument] = Field(
        default_factory=list,
        description="List of source documents retrieved via RAG"
    )
    confidence: Optional[float] = Field(
        None,
        description="Optional confidence score (0.0-1.0) if available"
    )
