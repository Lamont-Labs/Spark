# FILE: tools/generate_sbom.py
"""
Spark™ v2.3 — Deterministic SBOM Generator (placeholder)
Produces a compact CycloneDX-like JSON with file hashes for key demo artifacts.
"""

from __future__ import annotations
import hashlib, json, os, time

ROOT = os.path.dirname(os.path.dirname(__file__))
SBOM_DIR = os.path.join(ROOT, "SBOM")
os.makedirs(SBOM_DIR, exist_ok=True)

TARGETS = [
    "requirements.txt",
    "cli/seed_entries.py",
    "src/core/streak_engine.py",
    "provenance/streak_result.json",
]

def sha256_of(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()

components = []
for rel in TARGETS:
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path):
        continue
    components.append({
        "type": "file",
        "name": rel,
        "hashes": [{"alg": "SHA-256", "content": sha256_of(path)}]
    })

sbom = {
    "bomFormat": "CycloneDX",
    "specVersion": "1.5-min",
    "version": 1,
    "metadata": {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "component": {"name": "SparkApp", "type": "application", "version": "v2.3"},
        "authors": ["Jesse J. Lamont"],
    },
    "components": components,
}

out_path = os.path.join(SBOM_DIR, "sbom.cdx.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(sbom, f, indent=2)
print(f"[✓] SBOM written → {out_path}")
