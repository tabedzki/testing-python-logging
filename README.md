# testing-nested-logging

The logger is defined within the `__init__.py` which is run before `__main__.py` and the first time someone runs `import testing_logging` which ensures that the module level logger for the package is always defined.

## Installation

Please install as a package by doing

```bash
git clone git@github.com:tabedzki/testing-python-logging.git
cd testing-python-logging
pip install -e .
```

## Executing

The code can be run by using the code as a module

```bash
python -m testing_logging
```

or run as a library through the example script

```sh
python outer_and_inner_logger.py
```

Alternatively, if you wish to pipe stderr to a file run `python outer_and_inner_logger.py > console.log 2>&1`.


