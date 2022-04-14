#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="QuaCoPy",
    version="0.0.1",
    description="Quantum Computing Simulation for Python",
    author="Lukas Reithmeier",
    url="https://github.com/reithmeier/PythonArchetype",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Optional
)
