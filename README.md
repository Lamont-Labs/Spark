# FILE: README.md
# Spark™ — Gratitude, Wins & Affirmations App  
*Version:* v2.3 • *Date:* 2025-10-05 • *Owner:* Jesse J. Lamont  
[![sparkapp-demo-ci](https://github.com/Lamont-Labs/Spark/actions/workflows/ci.yml/badge.svg)](https://github.com/Lamont-Labs/Spark/actions/workflows/ci.yml)
## 🌟 Overview  
Spark™ helps users build gratitude and self-reflection habits through short daily entries — Gratitude, Wins, and Affirmations.  
It’s designed for **kids, teens, and adults**, featuring **adaptive prompts**, **bend-not-break streaks**, and an **offline-first experience**.  

## 🎯 Key Features  
- Daily reflection prompts  
- Adaptive modes (Kid / Teen / Parent)  
- Bend-not-break streaks  
- Offline SQLite storage  
- Optional AI summaries (stubbed)  

## 🧱 Architecture  
Hybrid demo:  
- React Native UI via Expo  
- Local Python streak engine  
- SQLite local storage  

## ⚙️ Getting Started  
See [docs/QUICKSTART.md](docs/QUICKSTART.md)

## 🔒 Provenance  
Deterministic demo — all artifacts reproducible.  
Verify hashes via:  
```bash
bash verify.sh
