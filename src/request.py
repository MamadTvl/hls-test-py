import requests
import time


class RequestsClient():
    def download(self, uri, timeout=None, headers={}, verify_ssl=True) -> tuple[str, str]:
        o = requests.get(uri, timeout=timeout, headers=headers)
        return o.text, o.url
