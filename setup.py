#!/usr/bin/env python

from setuptools import setup, find_packages

description = ("A high level quantum circuit API over tensornetwork.")

# Reading long Description from README.md file.
with open("README.md", "r") as readme:
  long_description = readme.read()

# Read in requirements
requirements = [ requirement.strip() \
                 for requirement in open("requirements.txt").readlines() ]

setup (
  name="qcsimulator",
  version="0.1.0",
  url="https://github.com/katolikyan/QCSimulator",
  author="Tigran Katolikyan",
  author_email="tigrankatolikyan@gmail.com",
  python_requires=(">=3.6.0"),
  install_requires=requirements,
  license="Apache 2.0",
  description=description,
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=find_packages(),
)
