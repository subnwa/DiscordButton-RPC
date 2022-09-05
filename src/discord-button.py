from http.client import InvalidURL


def button(label: str, url: str):
    if any(v in url for v in url):
        payloads = {"label": label, "url": url}
        link = {"link": url, "label": label}
        return button
    else:
        raise InvalidURL + TypeError("Invalid URL passed")
    pass


class RPC(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = 'Error: ' + message
        super().message = message

    pass


class images(Exception):
    def __init__(self, message: str = None):
        var = (v in images for v in images)
        image = {"image": images, "type": images.get("type")}
        image = format(format(image, var))

    @classmethod
    def get(cls, param):
        pass


class ButtonError(RPC):
    def __init__(self, message: str = None):
        super().message = message
        message = 'Error: ButtonError (RPC)'

    pass


def button(
        button_one_label: str = None, ):
    if button_one_label is None:
        raise ButtonError('None')

    return
