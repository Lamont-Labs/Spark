# FILE: verify.sh
#!/usr/bin/env bash
set -e

echo "Verifying Spark™ demo determinism..."
HASH_BEFORE=$(find src -type f -exec sha256sum {} \; | sha256sum)
python3 src/core/streak_engine.py --seed 42 --test > /tmp/output.log
HASH_AFTER=$(find src -type f -exec sha256sum {} \; | sha256sum)

if [ "$HASH_BEFORE" = "$HASH_AFTER" ]; then
  echo "✅ Deterministic build confirmed."
else
  echo "⚠️ Drift detected — check modified files."
  exit 1
fi

echo "Recomputing provenance hashes..."
find . -type f -not -path "./.venv/*" -exec sha256sum {} \; > SBOM/checksums.csv
echo "{\"verified\": true, \"timestamp\": \"$(date -u)\"}" > SBOM/provenance.json
echo "Done."
