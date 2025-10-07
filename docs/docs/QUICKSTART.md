# FILE: docs/QUICKSTART.md
## 🏁 Quickstart — Spark™ v2.3 Demo
Estimated time: 3 minutes.

### Prerequisites
- Node ≥ 18 (Expo CLI installed)
- Python ≥ 3.10
- No network required — offline demo

### Steps
```bash
git clone https://github.com/Lamont-Labs/SparkApp_v2.3.git
cd SparkApp_v2.3
make init_all
python3 cli/seed_entries.py
bash verify.sh
