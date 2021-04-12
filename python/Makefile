.PHONY: docs

PACKAGE_FOLDER = __name_of_package_folder__
LANG_FOLDER = "$(PACKAGE_FOLDER)/__name_of_lang_subfolder_"
DEMO_FOLDER = __name_of_demo_folder__

help:
	@echo "check"
	@echo "cover"
	@echo "notes"
	@echo "flake"
	@echo "lint-e"
	@echo "lint"
	@echo "lint-demo"
	@echo "ver"
	@echo "upload"
	@echo "docs"
	@echo "po"
	@echo "mo"
	@echo "uml"
	@echo "run-warn"

check:
	@nose2 -vvv --with-coverage

cover:
	@nose2 --with-coverage --coverage-report=html

notes:
	@rgrep "TODO" --include="*py" --include="*md" --include="*rst" --exclude="release-checklist.md" || true
	@rgrep "# REF" --include="*py" || true

flake:
	flake8 $(PACKAGE_FOLDER)

lint-e:
	pylint --disable=R,C,W $(PACKAGE_FOLDER) || true

lint:
	pylint $(PACKAGE_FOLDER) || true

lint-demo:
	pylint $(DEMO_FOLDER) || true

docs:
	sphinx-build docs/source/ docs/build/

	sphinx-build -b latex docs/source/ docs/build/latex
	pdflatex -output-directory docs/build/latex docs/build/latex/$(PACKAGE_FOLDER).tex
	cp docs/build/latex/$(PACKAGE_FOLDER).pdf ./

ver:
	@cat $(PACKAGE_FOLDER)/__init__.py | grep __version__

upload:
	python3 setup.py sdist
	python3 -m twine upload --repository pypi dist/*

po:
	for f in $(PACKAGE_FOLDER)/*.py; do \
		s=$${f##*/} ; \
		fo=$(LANG_FOLDER)/$${s%%.*}.po ; \
		if [ -f $$fo ] ; then \
			xgettext $$f -j --no-location -o $$fo ; \
		else \
			xgettext $$f --no-location -o $$fo ; \
		fi ; \
		if [ -f $$fo ] ; then \
			msginit --no-translator --input=$$fo --locale=ru_RU.UTF-8 -o $$fo ; \
		fi ; \
	done

mo:
	for f in $(LANG_FOLDER)/*.po; do \
		msgfmt "$$f" -o "$${f%%.*}.mo"; \
	done

run-warn:
	python3 -W all ./gui

uml:
	pyreverse3 $(PACKAGE_FOLDER) -o png