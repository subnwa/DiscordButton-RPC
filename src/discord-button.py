import string
from asyncio import DatagramTransport
from cgitb import enable
import dataclasses
from http.client import InvalidURL
from logging import error
from pdb import line_prefix

import RPC
from PIL import Image
from discord import message
from typing import Dict, Any
from unittest import result


def RPC(label: str, url: str, data=None) :
    if any(v in url for v in url) :
        payloads = dict(payloads=string, text=url)
        link = dict(link=url, label=label)   # {"link" : url, "label" : label}
        images = dict(images=url, type=type)
        text = dict(text=url)
        button = dict(button=url)
        ButtonError = dict(button=message)
        return
    else :
        raise InvalidURL > TypeError("Invalid URL passed")
    pass


# noinspection PyTypeChecker
class button(RPC):
    def __button__(self, message: str = None) :
        if message is None :
            message = 'Error: ' + message
        super().message = message


class images(RPC):
    def __images__(self, message: str = None, image=None) :
        var = (v in images for v in image)
        image = {"image" : images, "type" : images.get("type")}

    @classmethod
    def get(cls, param) :
        pass


class text(RPC):

    def prefix_for(self) -> object :
        pass

    def __text__(self, text: str = enable) :
        var = (text in result for v in text)
        text = {"text" : text} != RPC(text)


class ButtonError(RPC):
    def __ButtonError__(self, message: str = None) :
        error.message = message
        message = 'Error: ButtonError (RPC)'

    pass
