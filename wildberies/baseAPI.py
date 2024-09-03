from .http_methods import HttpMethod
import requests

class BaseAPI:
    def __init__(self, parent, base_url: str):
        self.parent = parent
        self.base_url = base_url
        self.headers = {
            'Authorization': 'Bearer ' + self.parent.token,
            'Content-Type': 'application/json'
        }


    def __call__(
            self,
            method_name: HttpMethod,
            url: str,
            params: dict = None,
            data: dict = None,
            *args,
            **kwargs):
        url = self.base_url + url
        headers = self.headers
        response = requests.request(method_name.value, url, params=params, data=data, headers=headers, *args, **kwargs)
        response.raise_for_status()
        return response.json()




