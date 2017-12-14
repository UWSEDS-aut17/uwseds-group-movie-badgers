#!/bin/bash

# run this script via: bash run.sh

# run the unit tests
nosetests --with-coverage test_clean_data.py test_get_data.py test_model.py test_visual.py

# run the PEP8 checker
pycodestyle test_clean_data.py test_get_data.py test_model.py test_visual.py

cd ..\

pycodestyle clean_data.py get_data.py regression_model.py movie_plot.py
