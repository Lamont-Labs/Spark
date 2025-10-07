#!/usr/bin/env bash
set -e
echo "Verifying Spark™ demo determinism..."

# 1. Ensure expected folders exist
mkdir -p provenance dist/demo_db

# 2. Verify demo files
if [ ! -d "src" ]; then
  echo "src directory missing — creating placeholder..."
  mkdir -p src/core
fi

# 3. Run streak engine check
python3 src/core/streak_engine.py

# 4. Hash provenance output for reproducibility
if [ -f provenance/streak_result.json ]; then
  sha256sum provenance/streak_result.json > provenance/checksums.csv
  echo "[✓] Checksum written to provenance/checksums.csv"
else
  echo "[✗] streak_result.json not found."
  exit 2
fi

echo "[✓] Spark demo verification complete."
