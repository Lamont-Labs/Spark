# FILE: docs/QA_CHECKLIST.md
## Demo Readiness Checklist
- [x] Offline run verified (`expo start`)  
- [x] Streak engine produces consistent results (seed 42)  
- [x] SQLite demo DB generates and loads  
- [x] verify.sh passes checksum comparison  
- [x] SBOM present in / SBOM folder  
- [x] No unverified dependencies added  

## CI Targets (planned)
- Lint JS + Python  
- Jest unit tests (streak logic)  
- Pytest integration (streak recovery)  
- Determinism recheck  

## Definition of Green
> “A fresh clone runs demo successfully and hashes match golden values.”
