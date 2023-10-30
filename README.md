# beans_logging_fastapi

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bybatkhuu/module.fastapi-logging/2.build-publish.yml?logo=GitHub)](https://github.com/bybatkhuu/module.fastapi-logging/actions/workflows/2.build-publish.yml)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/bybatkhuu/module.fastapi-logging?logo=GitHub)](https://github.com/bybatkhuu/module.fastapi-logging/releases)

`beans_logging_fastapi` is a template for python package.

## Features

- Template for python package.
- Other features...

---

## Installation

### 1. Prerequisites

- **Python (>= v3.7)**
- **PyPi (>= v21)**

### 2. Install beans-logging-fastapi package

Choose one of the following methods to install the package **[A ~ F]**:

**A.** [**RECOMMENDED**] Install from **PyPi**

```sh
# Install or upgrade package:
pip install -i https://test.pypi.org/simple -U beans-logging-fastapi
```

**B.** Install latest version from **GitHub**

```sh
# Install package by git:
pip install git+https://github.com/bybatkhuu/module.fastapi-logging.git
```

**C.** Install from **pre-built release** files

1. Download **`.whl`** or **`.tar.gz`** file from **releases** - <https://github.com/bybatkhuu/module.fastapi-logging/releases>
2. Install with pip:

```sh
# Install from .whl file:
pip install ./beans_logging_fastapi-[VERSION]-py3-none-any.whl
# Or install from .tar.gz file:
pip install ./beans_logging_fastapi-[VERSION].tar.gz
```

**D.** Install from **source code** by building package

```sh
# Clone repository by git:
git clone https://github.com/bybatkhuu/module.fastapi-logging.git beans_logging_fastapi
cd ./beans_logging_fastapi

# Install python build tool:
pip install -U pip build

# Build python package:
python -m build

_VERSION=$(./scripts/get-version.sh)

# Install from .whl file:
pip install ./dist/beans_logging_fastapi-${_VERSION}-py3-none-any.whl
# Or install from .tar.gz file:
pip install ./dist/beans_logging_fastapi-${_VERSION}.tar.gz
```

**E.** Install with pip editable **development mode** (from source code)

```sh
# Clone repository by git:
git clone https://github.com/bybatkhuu/module.fastapi-logging.git beans_logging_fastapi
cd ./beans_logging_fastapi

# Install with editable development mode:
pip install -e .
```

**F.** Manually add to **PYTHONPATH** (not recommended)

```sh
# Clone repository by git:
git clone https://github.com/bybatkhuu/module.fastapi-logging.git beans_logging_fastapi
cd ./beans_logging_fastapi

# Install python dependencies:
pip install -r ./requirements.txt

# Add current path to PYTHONPATH:
export PYTHONPATH="${PWD}:${PYTHONPATH}"
```

## Usage/Examples

To use `beans_logging_fastapi`, import the `MyBase` class from the package:

```python
from beans_logging_fastapi import MyBase, BaseConfig

my_base = MyBase()
```

### **Simple**

[**`main.py`**](https://github.com/bybatkhuu/module.fastapi-logging/blob/main/examples/simple/main.py)

```python
import sys
import logging

from beans_logging_fastapi import MyBase


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    _my_base = MyBase(item="item-01")
    logger.info(f" My item => {_my_base.item}")
```

Run the [**`examples/simple`**](https://github.com/bybatkhuu/module.fastapi-logging/tree/main/examples/simple):

```sh
cd ./examples/simple

python ./main.py
```

**Output**:

```txt
INFO:__main__: My item => item-01
```

---

## Running Tests

To run tests, run the following command:

```sh
# Install python test dependencies:
pip install -r ./requirements.test.txt

# Run tests:
python -m pytest -sv
```

## Environment Variables

You can use the following environment variables inside [**`.env.example`**](https://github.com/bybatkhuu/module.fastapi-logging/blob/main/.env.example) file:

```sh
# ENV=development
# DEBUG=true
```

## Documentation

- [docs](https://github.com/bybatkhuu/module.fastapi-logging/blob/main/docs/README.md)
- [scripts](https://github.com/bybatkhuu/module.fastapi-logging/blob/main/docs/scripts/README.md)

---

## References

- Python Packaging User Guide - <https://packaging.python.org>
- Python Packaging Tutorial - <https://packaging.python.org/en/latest/tutorials/packaging-projects>
