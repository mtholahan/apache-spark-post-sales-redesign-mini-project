#!/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$HOME/pyspark_venv"
OUTPUT_DIR="$SCRIPT_DIR/output"

echo "🔧 Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "🧹 Cleaning output..."
rm -rf "$OUTPUT_DIR"

echo "🚀 Running Spark job..."
spark-submit "$SCRIPT_DIR/autoinc_spark.py"

echo "✅ Job complete. Output at: $OUTPUT_DIR"

echo "🔻 Deactivating..."
deactivate

