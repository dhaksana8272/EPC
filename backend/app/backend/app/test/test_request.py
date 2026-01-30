from app.schemas.request import EPCQueryRequest

# ✅ Valid request with all fields
data_full = {
    "query": "Explain transformer grounding standards",
    "branch": "Electrical",
    "document_name": "epc_electrical_specs.pdf"
}
request_full = EPCQueryRequest(**data_full)
print("Full request:", request_full)

# ✅ Valid request with only query (free-form)
data_min = {"query": "How do we mitigate vendor delays?"}
request_min = EPCQueryRequest(**data_min)
print("Minimal request:", request_min)

# ❌ Invalid request (missing query)
try:
    EPCQueryRequest(branch="Civil")
except Exception as e:
    print("Validation Error:", e)
