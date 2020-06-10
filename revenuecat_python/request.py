import requests
from .error import RevenueCatError


def basic_auth_request(method, url, token=None, platform=None, payload=None, params=None):
    request_kwargs = {}
    if token is not None:
        request_kwargs["headers"] = {
            "Authorization": "Bearer {0}".format(token),
            "Content-Type": "application/json",
            "X-Platform": None if not platform else platform.value,
        }
    if payload is not None:
        request_kwargs["json"] = payload
    if params is not None:
        request_kwargs["params"] = params

    response = requests.request(method, url, **request_kwargs)

    if response.status_code not in (200, 201):
        raise RevenueCatError(message=response.json().get('message'), http_status=response.status_code, json_body=response.json(), headers=response.headers)

    return response.json()
