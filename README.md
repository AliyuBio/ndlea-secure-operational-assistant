## 📂 Repository File Registry & Descriptions

To make navigating and reproducing this project seamless, here is a breakdown of each file included in this repository and its exact operational role:

### ⚙️ Core Configuration & Validation Files
* **`metadata.json`**  
  The official challenge configuration manifest containing team parameters, problem domains, bonus track claims (budget laptop environment), and our definitive evaluation test prompts.
* **`download_model.sh`**  
  An automated shell script that handles the secure retrieval of our optimized 4-bit quantized `Phi-3-Mini-4K-Instruct` GGUF model weights directly from the huggingface cache repository to local storage.
* **`.gitignore`**  
  Prevents heavy runtime assets, local benchmarking logs (`submission.json`), and raw model weight folders (`model/*.gguf`) from tracking to GitHub to maintain clean repository versions.
* **`requirements.txt`**  
  The Python ecosystem manifest specifying the pinned versions of our local pipeline components (including Streamlit, llama-cpp-python, sentence-transformers, and ChromaDB).

### 🖥️ Application Logic & Database Files
* **`app.py`**  
  The primary user interface engine built on Streamlit. It manages the multi-view split-screen interface, handling user interactions, field data capture, and displaying the analytical response panels.
* **`engine.py`**  
  The decoupled algorithmic backend driving the offline architecture. It handles document parsing, vector extraction/matching inside the persistent disk instance, and triggers the local context token generation stream.

### 📝 Documentation & Reports
* **`REPORT.md`**  
  Our comprehensive technical report detailing our system constraints, architectural design decisions, hardware profiling thresholds, and performance metrics.
* **`README.md`**  
  The primary entry point for users, containing setup guidelines, deployment steps, repository manifests, and execution commands.
