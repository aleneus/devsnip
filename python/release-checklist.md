# Python project release checklist

## Test

* All passed: `make check`
* Coverage >= __%: `make check`
* All manual tests pass (`test/manual`)

## Code

* No TODO notes: `make notes`
* No flakes: `make flake`
* No lint errors: `make lint-e`
* Lint result >= __: `make lint`
* Old deprecated code is removed (todo list)

## Docs

* Successful build: `make docs`
* History is updated: `head -n 20 docs/source/history.rst`

## Distribution

* Actual version: `make ver`
* All used libraries are fresh
* Installation successful: `python3 setup.py install --user`
* Examples from README.md work after installation
* All utilities work after installation
* All package data are relevant

## Demo

* All examples work: `./run-demo.sh`

## Translation

* No empty entries in *po files: `make po`
* Translation files compiled succesfully: `make mo`

## Windows

* Python interpreter runs application: `py <name>`
* Build successful
* Application works on clear machine
