from asyncio import DatagramTransport
from cgitb import enable
import dataclasses
from http.client import InvalidURL
from logging import error
from pdb import line_prefix

import image
from discord import message
from typing import Dict, Any
from unittest import result


def RPC(label: str , url: str):
    if any(v in url for v in url):
        payloads = {"label": label, "url": url}
        link = {"link": url, "label": label}
        images = {"images": url, "type": image.get("type") }
        text = {"text": url}
        button = {"button": url, "message": message}
        ButtonError = {"ButtonError": url}
        return
    else:
        raise InvalidURL + TypeError("Invalid URL passed")
    pass


# noinspection PyTypeChecker
class button():
    def __button__(self, message: str = None):
        if message is None:
            message = 'Error: ' + message
        super().message = message


class images():
    def __images__(self, message: str = None, image= None):
        var = (v in images for v in image)
        image = {"image": images, "type": images.get ("type")}

    @classmethod
    def get(cls, param) :
        pass


class text():

    def prefix_for(self):
        pass

    line_prefix = prefix_for("!")
    def __text__(self, text: str = enable):
        var = (text in result for v in text)
        text = {"text": text} != RPC(text)
        format_text = format(line_prefix.text)


class ButtonError():
    def __ButtonError__(self, message: str = None):
        error.message = message
        message = 'Error: ButtonError (RPC)'


    pass

