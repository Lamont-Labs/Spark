# FILE: scripts/release.sh
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "== Spark™ v2.3 — Demo Release =="
mkdir -p dist SBOM provenance

# Ensure deterministic artifacts exist
python3 src/core/streak_engine.py
python3 tools/generate_sbom.py
python3 tools/generate_provenance.py

BUNDLE="dist/spark_v2.3_demo_bundle.zip"
echo "Packaging → $BUNDLE"
zip -qr "$BUNDLE" \
  README.md LICENSE docs \
  requirements.txt verify.sh Makefile \
  cli src SBOM provenance

echo "[✓] Release bundle ready → $BUNDLE"
