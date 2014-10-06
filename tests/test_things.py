"""
This module tests something ...

Install pip install pytest

Run with py.test test_things.py

"""

import pytest  # This is the Python test runner we use
# http://pytest.org/latest/getting-started.html#getstarted


# put some tests here
def test_thing():
    """This is a typical python unit test"""
    from wrapup.my_code import main

    result = main()
    assert result == u'Hello World!'


