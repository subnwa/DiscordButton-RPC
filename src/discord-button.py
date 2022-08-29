from http.client import InvalidURL


def button_one(label: str, url: str):
    if any(v in url for v in test_url):
        payloads = {"label": label, "url": url}
        return payloads
    else:
        raise InvalidURL + TypeError("Invalid URL passed")


class RPC(Exception):
    def __init__(self, message: str = None):
        if message is None:
            message = 'Error: ' + message
        super().__init__(message)


class ButtonError(RPC):
    def __init__(self, message: str = None):
        super().__init__(message)

    pass


test_url = ["https://", "http://", "https://"]


def button(
        button_one_label: str = None, ):
    if button_one_label is None:
        raise ButtonError('"button_one_label" cannot None')

    return
