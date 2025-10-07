.PHONY: sbom

sbom:
	@echo "Generating SBOM (placeholder)"
	@mkdir -p SBOM
	@echo '{ "sbom": "CycloneDX placeholder for SparkApp v2.3", "generated_at": "'$$(date -u +'%Y-%m-%dT%H:%M:%SZ')" }' > SBOM/sbom.cdx.json
	@echo "[✓] SBOM written to SBOM/sbom.cdx.json"
