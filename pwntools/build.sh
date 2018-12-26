#!/bin/bash

# clone the source
git clone --depth 1 https://github.com/Gallopsled/pwntools.git
cd pwntools/docs

# install the requirements through pipenv
pipenv install --two -r requirements.txt
pipenv shell
# the following is required on my computer. Don't know why :(
pip install PySocks
pip install psutil
pip install intervaltree
pip install python-dateutil
pip install packaging

# build it!
make dash
