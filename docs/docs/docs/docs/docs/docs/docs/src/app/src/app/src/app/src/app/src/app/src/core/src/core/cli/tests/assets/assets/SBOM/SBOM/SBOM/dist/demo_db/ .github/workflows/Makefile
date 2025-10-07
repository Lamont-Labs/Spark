# FILE: Makefile
PROJECT = SparkApp
VERSION = v2.3

init_all:
	@echo "Initializing $(PROJECT) $(VERSION)"
	python3 cli/seed_entries.py

demo:
	@echo "Running SparkApp demo..."
	cd src/app && npx expo start

verify:
	bash verify.sh

sbom:
	@echo "Generating SBOM..."
	mkdir -p SBOM
	echo '{"demo":"sbom"}' > SBOM/sbom.cdx.json

clean:
	rm -rf dist/demo_db/spark_demo.sqlite
	rm -f tmp_hashes.csv

.PHONY: init_all demo verify sbom clean
