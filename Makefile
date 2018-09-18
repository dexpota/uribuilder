PYPI_SERVER = pypitest

.PHONY: release
release: sdist wheel clean ## Package and upload release
	@echo "+ $@"
	@twine upload -r $(PYPI_SERVER) dist/*

.PHONY: sdist
sdist: clean ## Build sdist distribution
	@echo "+ $@"
	@pipenv run python setup.py sdist
	@ls -l dist

.PHONY: wheel
wheel: clean ## Build bdist_wheel distribution
	@echo "+ $@"
	@pipenv run python setup.py bdist_wheel
	@ls -l dist

.PHONY: clean
clean: ## Remove all artifacts 
	@echo "+ $@"

.PHONY: test
test:
	@tox	

requirements-dev.txt: Pipfile.lock ## Generate requirements file for developing from Pipenv.
	@echo "+ $@"
	@pipenv lock --requirements --dev > requirements-dev.txt

requirements.txt: Pipfile.lock ## Generate requirements file from Pipenv
	@echo "+ $@"
	@pipenv lock --requirements > requirements.txt
