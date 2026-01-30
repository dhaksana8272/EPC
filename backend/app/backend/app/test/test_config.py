from ..core.config import *

print("BASE_DIR:", BASE_DIR)
print("RAW_DOCS_DIR exists:", RAW_DOCS_DIR.exists())
print("VECTOR_DB_DIR exists:", VECTOR_DB_DIR.exists())
print("Embedding model:", EMBEDDING_MODEL_NAME)
print("LLM model:", LLM_MODEL_NAME)
