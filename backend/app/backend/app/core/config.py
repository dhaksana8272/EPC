from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]

# =========================
# DATA DIRECTORIES
# =========================
RAW_DOCS_DIR = BASE_DIR / "data" / "raw_docs"
PROCESSED_DOCS_DIR = BASE_DIR / "data" / "processed_docs"

# =========================
# VECTOR DATABASE (CRITICAL)
# =========================
# 🔴 MUST point to the SAME location used by ingest.py
VECTOR_DB_DIR = Path(
    r"D:\\L&T - Copy 3\\backend\\app\\vector_db"  # <-- CHANGE ONLY IF NEEDED
)

TOP_K = 5

# =========================
# EMBEDDING MODEL
# =========================
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# =========================
# LLM CONFIGURATION
# =========================
LLM_MODEL_NAME = "microsoft/phi-3-mini-4k-instruct"
MAX_TOKENS = 1024
TEMPERATURE = 0.2
DEVICE = os.getenv("DEVICE", "cpu")

# =========================
# API CONFIG
# =========================
APP_NAME = "EPC Reasoning Engine"
APP_VERSION = "1.0.0"

# =========================
# CREATE REQUIRED DIRECTORIES
# =========================
# ✅ Safe to auto-create
for directory in [
    RAW_DOCS_DIR,
    PROCESSED_DOCS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# =========================
# VECTOR DB VALIDATION
# =========================
if not VECTOR_DB_DIR.exists():
    raise RuntimeError(
        f"❌ Vector DB directory not found at {VECTOR_DB_DIR}. "
        f"Run ingest.py first."
    )

if not any(VECTOR_DB_DIR.iterdir()):
    raise RuntimeError(
        f"❌ Vector DB directory is EMPTY at {VECTOR_DB_DIR}. "
        f"FAISS index not found."
    )