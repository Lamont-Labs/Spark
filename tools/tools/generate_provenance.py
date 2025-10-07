# FILE: tools/generate_provenance.py
"""
Spark™ v2.3 — Provenance Emitter
Writes SBOM/provenance.json with commit, timestamps, and key artifact hashes.
"""

from __future__ import annotations
import hashlib, json, os, time, subprocess

ROOT = os.path.dirname(os.path.dirname(__file__))
SBOM_DIR = os.path.join(ROOT, "SBOM")
PROV_DIR = os.path.join(ROOT, "provenance")
os.makedirs(SBOM_DIR, exist_ok=True)
os.makedirs(PROV_DIR, exist_ok=True)

def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()

def git_rev() -> str:
    env_sha = os.getenv("GITHUB_SHA")
    if env_sha:
        return env_sha
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip()
    except Exception:
        return "local-working-copy"

artifacts = [
    ("requirements.txt", os.path.join(ROOT, "requirements.txt")),
    ("cli/seed_entries.py", os.path.join(ROOT, "cli/seed_entries.py")),
    ("src/core/streak_engine.py", os.path.join(ROOT, "src/core/streak_engine.py")),
    ("provenance/streak_result.json", os.path.join(ROOT, "provenance/streak_result.json")),
]

entries = []
for name, path in artifacts:
    if os.path.isfile(path):
        entries.append({"path": name, "sha256": sha256(path)})

payload = {
    "project": "SparkApp",
    "version": "v2.3",
    "owner": "Jesse J. Lamont",
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "commit": git_rev(),
    "artifacts": entries,
}

out_path = os.path.join(SBOM_DIR, "provenance.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2)
print(f"[✓] Provenance written → {out_path}")
