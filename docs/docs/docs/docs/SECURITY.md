# FILE: docs/SECURITY.md
## Data Handling
- Offline by default — no external API calls.  
- Local SQLite DB stored in `dist/demo_db/`.  
- `.env.example` configurable path and seed.  

## Supply Chain
- All Python deps pinned in requirements.txt.  
- Expo modules locked via package-lock.json (TBD).  
- SBOM generated through `make sbom`.  

## Provenance
- `verify.sh` recomputes SHA-256 hashes across repo.  
- Results logged in `SBOM/checksums.csv`.  

## Threat Model
- Attack surface restricted to local device.  
- No sensitive data transmitted.  
- Demo code runs sandboxed in Expo environment.  

## Known Gaps
- No PIN lock or encryption of entries yet.  
- No network authentication layer (offline only).  
- Security review scheduled post MVP.
