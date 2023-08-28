#!/bin/bash

python -m pip install --upgrade pip
pip install --upgrade setuptools
pip install wheel
pip install tox
echo
which python
which pip
which tox
echo
python --version
pip --version
tox --version
echo
pip list
