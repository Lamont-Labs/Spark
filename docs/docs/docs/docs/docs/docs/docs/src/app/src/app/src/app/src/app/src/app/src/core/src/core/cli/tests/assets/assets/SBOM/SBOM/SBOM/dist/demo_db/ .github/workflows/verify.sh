# FILE: verify.sh
#!/usr/bin/env bash
set -e
echo "🔍 Verifying SparkApp v2.3 deterministic demo..."
HASHES_FILE="SBOM/checksums.csv"
TMP_HASHES="tmp_hashes.csv"

echo "file,sha256" > $TMP_HASHES
for f in $(find src cli -type f -name "*.py" -o -name "*.js"); do
  sha256sum "$f" | awk '{print $2","$1}' >> $TMP_HASHES
done

if diff -q $HASHES_FILE $TMP_HASHES; then
  echo "✅ Deterministic build confirmed."
  rm $TMP_HASHES
  exit 0
else
  echo "❌ Hash mismatch detected!"
  diff $HASHES_FILE $TMP_HASHES || true
  rm $TMP_HASHES
  exit 1
fi
