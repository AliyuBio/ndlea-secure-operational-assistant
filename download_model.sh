#!/bin/bash
# Idempotent script to safely fetch GGUF weights for evaluation
mkdir -p model

MODEL_URL="https://huggingface.co/bartowski/Phi-3-mini-4k-instruct-GGUF/resolve/main/Phi-3-mini-4k-instruct-Q4_K_M.gguf"
TARGET_PATH="model/phi-3-mini-4k-instruct-q4.gguf"

if [ ! -f "$TARGET_PATH" ]; then
    echo "Downloading optimized Phi-3 GGUF model weights..."
    curl -L "$MODEL_URL" -o "$TARGET_PATH"
else
    echo "Model weights already cached locally."
fi