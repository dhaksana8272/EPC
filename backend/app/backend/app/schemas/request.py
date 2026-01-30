from pydantic import BaseModel, Field
from typing import Optional

class EPCQueryRequest(BaseModel):
    """
    Request schema for EPC Reasoning Engine.
    - Accepts any user query about EPC documents.
    - Optional branch to hint at the domain (Civil, Mechanical, Electrical, etc.)
    - Optional document name if the user wants to query a specific EPC file.
    """

    query: str = Field(
        ...,
        description="User question related to EPC documents. Free-form, any natural language."
    )

    branch: Optional[str] = Field(
        None,
        description="Optional EPC engineering branch hint (Civil, Electrical, Mechanical, Instrumentation, etc.)"
    )

    document_name: Optional[str] = Field(
        None,
        description="Optional: Specific EPC document filename to query from"
    )
