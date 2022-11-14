# Release checklist

## Auto check

* No errors: `make check`
* Coverage by tests >= __%

## Acceptance

* All manual tests passed (`test/manual`)
* Random working with UI: __ minutes

## Code quality

* Lint result >= __: `make lint`
* Old deprecated code is removed (todo list)

## Docs

* Successful build: `make docs`
* History is updated: `head -n 20 docs/source/history.rst`

## Distribution

* Actual version: `make ver`
* All used libraries are fresh
* Installation successful: `python3 setup.py install .`
* Examples from README.md work after installation
* All utilities work after installation
* All package data are relevant

## Demo

* All examples work: `./sh/run-demo.sh`

## Translation

* No empty entries in *po files: `make po`
* Translation files compiled succesfully: `make mo`

## Windows

* Python interpreter runs application: `py <name>`
* Build successful
* Application works on clear machine
