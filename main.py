import os

import self as self
from setuptools import setup, find_packages

auto_start = True

if not setup:
    raise ImportError("No setup specified")
    # if setup is not available, we need to make sure to install it

f = open("README.md")

