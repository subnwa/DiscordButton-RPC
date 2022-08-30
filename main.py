import os

import self as self
from setuptools import setup, find_packages

auto_start = True
error = OSError

if not setup:
    raise ImportError("No setup specified")
    # if setup is not available, we need to make sure to install it


class error(OSError):
    def __init__(self, msg: str):
        self.msg = msg
        msg = "OSError: %s" % msg


f = open("README.md")
execfile('discord-button.py')
