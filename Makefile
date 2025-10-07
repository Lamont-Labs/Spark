# FILE: Makefile
PROJECT=SparkApp_v2.3

init_all:
	@echo "Initializing local environment for $(PROJECT)"
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run_demo:
	@echo "Launching Spark demo (offline)"
	cd src/core && python streak_engine.py

verify:
	bash verify.sh

sbom:
	@echo "Generating SBOM (placeholder)"
	@echo '{"tool":"syft","result":"sbom.cdx.json"}' > SBOM/sbom.cdx.json

zip:
	@zip -r dist/$(PROJECT)_bundle.zip . -x "*.venv*" "__pycache__"
