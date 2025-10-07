# FILE: docs/ARCHITECTURE.md
## System Overview
Spark™ combines **Expo React Native** (frontend) and a **Python deterministic streak engine** for reproducibility.

### Components
- React Native app: screens for Today, History, Streaks, Settings  
- SQLite local DB: stores gratitude, wins, affirmations  
- Python core: streak engine, adaptive prompt logic  
- CLI tools: data seeding and verification  
- SBOM + provenance chain: for deterministic proofs  

### Data Flow
1. User enters daily Gratitude, Wins, Affirmations.  
2. SQLite persists locally.  
3. Streak engine evaluates continuity using bend-not-break logic.  
4. Periodic prompts update from `prompt_bank.json`.  
5. SBOM + provenance hashes generated via verify.sh.

### Integrations
Offline-first. Cloud sync and notifications deferred for future builds.
