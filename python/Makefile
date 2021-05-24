.PHONY: docs test

PACKAGE_FOLDER = __name_of_package_folder__
LANG_FOLDER = "$(PACKAGE_FOLDER)/__name_of_lang_subfolder_"
DEMO_FOLDER = __name_of_demo_folder__

help:
	@echo "check"
	@echo "test"
	@echo "todo"
	@echo "flake"
	@echo "lint-e"
	@echo "cover"
	@echo "lint"
	@echo "lint-demo"
	@echo "ver"
	@echo "docs"
	@echo "po"
	@echo "mo"
	@echo "upload"

	@echo "profile"
	@echo "run-warn"
	@echo "uml"

check: test todo flake line-e

test:
	@nose2 -vvv --with-coverage

todo:
	@rgrep "TODO" --include="*py" --include="*md" --include="*rst" --exclude="release-checklist.md" || true
	@rgrep "# REF" --include="*py" || true

flake:
	flake8 $(PACKAGE_FOLDER)

lint-e:
	pylint --disable=R,C,W $(PACKAGE_FOLDER) || true

cover:
	@nose2 --with-coverage --coverage-report=html

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

po:
	./sh/po.sh $(PACKAGE_FOLDER) $(LANG_FOLDER)

mo:
	./sh/mo.sh $(LANG_FOLDER)

upload:
	python3 setup.py sdist
	python3 -m twine upload --repository pypi dist/*

profile:
	python3 -m cProfile -s time ./gui

run-warn:
	python3 -W all ./gui

uml:
	pyreverse3 $(PACKAGE_FOLDER) -o png
