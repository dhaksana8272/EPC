from app.schemas.response import EPCQueryResponse, SourceDocument

# Create a mock response
mock_response = EPCQueryResponse(
    answer="Concrete safety requires proper curing and formwork checks.",
    branch="Civil",
    sources=[
        SourceDocument(
            name="epc_civil_specs.pdf",
            page=12,
            snippet="Ensure curing for at least 7 days at 20°C."
        ),
        SourceDocument(
            name="epc_civil_guidelines.pdf",
            page=3,
            snippet="Check formwork stability before pouring."
        )
    ],
    confidence=0.92
)

# Pydantic v2 method
print(mock_response.model_dump_json(indent=2))
