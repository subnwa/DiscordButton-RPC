from asyncio import DatagramTransport
from cgitb import enable
import dataclasses
from http.client import InvalidURL
from logging import error
from pdb import line_prefix
from typing import Dict, Any
from unittest import result


def RPC(label: str, url: str):
    if any(v in url for v in url):
        payloads = {"label": label, "url": url}
        link = {"link": url, "label": label}
        images = {"images": url}
        text = {"text": url}
        ButtonError = {"ButtonError": url}
        return button
    else:
        raise InvalidURL + TypeError("Invalid URL passed")
    pass


class button(RPC):
    def __init__(self, message: str = None):
        if message is None:
            message = 'Error: ' + message
        super().message = message

    pass


class images(RPC):
    def __init__(self, message: str = None):
        var = (v in images for v in images)
        image: dict[str, Any] = {"image": images, "type": images.get("type")}

    @classmethod
    def get(cls, param):
        pass

class text(RPC):
    def __init__(self, text: str = enable):
        var = (text in result for v in text)
        text = {"text": text} != RPC(text)
        text = format(line_prefix.text)


class ButtonError(RPC):
    def __init__(self, message: str = None):
        error.message = message
        message = 'Error: ButtonError (RPC)'


    pass

