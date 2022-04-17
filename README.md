# QuaCoPy - Quantum Computing Simulator for Python

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/reithmeier/QuaCoPy/blob/main/LICENSE)
[![Python Tests](https://github.com/reithmeier/QuaCoPy/workflows/Python%20Tests/badge.svg)](https://github.com/reithmeier/QuaCoPy/actions/workflows/python-tests.yml)
[![CodeQL](https://github.com/reithmeier/QuaCoPy/workflows/CodeQL/badge.svg)](https://github.com/reithmeier/QuaCoPy/actions/workflows/codeql-analysis.yml)


## Description

Simulate quantum computing using python. 
This project currently supports single QBits and two QBit registers.
Note that measurements are only simulated and there is currently no support for quantum simulators.

## Dependencies

* python
* pip

## Usage

Install Requirements

````shell
pip install -r requirements.txt
````

Install Project

````shell
pip install -e .
````

Start tox

````shell
tox
````