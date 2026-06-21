# 🦅 NDLEA Secure Operational Assistant

### 100% Offline, Air-Gapped Tactical Intelligence Hub & Relational Ledger

An infrastructure-grade edge computing application designed to run entirely on low-resource hardware thresholds (8 GB RAM). It empowers field units with semantic legal context parsing and secure operational asset logging with absolute zero cloud telemetry.

---

## 🚀 Core Architectural Modules
1. **Semantic Tactical Retrieval (RAG):** Extracts and maps sensitive PDFs into a local ChromaDB directory.
2. **Deterministic Inference Engine:** Queries a local Phi-3 model via Ollama, locked to low temperature to eliminate hallucinations.
3. **Isolated Relational Ledger:** Safely captures checkpoint metrics straight to a local SQLite3 database.

---

## 📦 Local Deployment Instructions
python -m pip install -r requirements.txt
python -m streamlit run app.py