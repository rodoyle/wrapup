# This is a Python Setup Script

import os
import re
from setuptools import setup

setup(
    name='wrapup',
    version='0.0.1',
    # long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),  # NOQA
    packages=['wrapup'],
    install_requires=[
        #Python requirements are listed here ie. 'thing', 'thing2', etc
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'run-wrapup = scripts/wrap:main',
        ],
    },
)
