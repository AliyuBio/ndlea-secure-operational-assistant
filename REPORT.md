# 🦅 NDLEA Secure Operational Assistant - Technical Report

## 1. Problem Definition
Enforcement units operating in rural boundaries require access to complex legal structures (such as Section 11 statutory penalties) and strict operational guidelines under conditions with zero cloud connectivity. This system provides a 100% offline, air-gapped solution utilizing optimized retrieval-augmented generation and an on-disk relational storage database ledger.

## 2. Hardware & Connectivity Constraints
* **RAM Profile:** Optimized strictly within an 8 GB threshold.
* **Network Isolation:** 100% air-gapped infrastructure. Zero web telemetry permitted post-deployment.
* **Storage Footprint:** Under 3.5 GB overall volume.

## 3. Design Decisions & Tools
* **Base Model:** Phi-3-Mini-4K-Instruct (3.8B Parameters).
* **Quantization Level:** Q4_K_M GGUF format for optimal throughput-to-accuracy ratios on low-spec host CPUs.
* **Runtime Driver:** Direct `llama-cpp-python` embedding matrix abstraction layer.
* **Vector Index:** ChromaDB processing local multi-stage chunk vector segments.

## 4. Development Benchmarks (Self-Reported)
* **Peak Memory Overhead:** ~4.1 GB RSS
* **Inference Speed:** ~16.5 Tokens per Second (TPS)
* **First Token Latency:** ~380ms