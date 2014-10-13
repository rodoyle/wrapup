"""
This module tests something ...

Install pip install pytest

Run with py.test test_things.py

"""

import pytest, os, sys  # This is the Python test runner we use
sys.path.append("../wrapup")
# http://pytest.org/latest/getting-started.html#getstarted

from wrapup.my_code import *

def test_read_csv():
    print ("\nTesting read_csv() function...\n")
    assert os.path.exists("data/spirals.csv")
    test = SpecClust("data/spirals.csv")
    assert test.get_rows() == 300
    assert test.get_cols() == 2

def test_cluster():
    print ("\nTesting cluster() function...\n")
    assert os.path.exists("data/spirals.csv")
    test = SpecClust("data/spirals.csv")
    test.set_centers(2)
    test.set_gamma(172.05)
    test.cluster()
    for i in range(1, test.get_rows()+1):
    	assert test.get_assignment(i) >= 1
    	assert test.get_assignment(i) <= 2

def test_write_csv():
    print ("\nTesting write_csv() function...\n")
    assert os.path.exists("data/spirals.csv")
    test = SpecClust("data/spirals.csv")
    test.set_centers(2)
    test.set_gamma(172.05)
    test.cluster()
    test.write_data("data/clustered.csv")
    assert os.path.exists("data/clustered.csv")
