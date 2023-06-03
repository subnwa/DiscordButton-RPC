import os


def execfile(param):
    pass


execfile('discord-button.py')

from setuptools import setup, find_packages

auto_start = True
error = OSError

if not setup:
    raise ImportError("No setup specified")
    # if setup is not available, we need to make sure to install it

f = open("README.md")


def parse_meta():
    with open(os.path.join("DiscordButton-RPC", "discord-button.py")) as fp:
        code = fp.read()

# print(parse_meta, f, error)

