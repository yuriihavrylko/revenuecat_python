from typing import Any, Dict

import httpx

from .enums import SubscriptionPlatform
from .responses import RevenueCatError, RevenueCatResponse


def _build_request(
    token: str = None,
    platform=None,
    payload: Dict[str, Any] = None,
    params: Dict[str, Any] = None,
) -> Dict[str, Any]:
    request_kwargs = {}
    if token is not None:
        request_kwargs["headers"] = {
            "Authorization": "Bearer {0}".format(token),
            "Content-Type": "application/json",
        }

        if platform:
            request_kwargs["headers"]["X-Platform"] = platform.value

    if payload is not None:
        request_kwargs["json"] = payload
    if params is not None:
        request_kwargs["params"] = params

    return request_kwargs


def _handle_response(response: httpx.Response) -> RevenueCatResponse:
    if response.status_code not in [200, 201]:
        raise RevenueCatError(
            message=response.json().get("message"),
            http_status=response.status_code,
            json_body=response.json(),
            headers=response.headers,
        )

    return RevenueCatResponse(
        http_status=response.status_code,
        json_body=response.json(),
        headers=response.headers,
    )


def basic_auth_request(
    method: str,
    url: str,
    token: str = None,
    platform: SubscriptionPlatform = None,
    payload: Dict[str, Any] = None,
    params: Dict[str, Any] = None,
) -> RevenueCatResponse:
    response = httpx.request(method, url, **_build_request(token, platform, payload, params))

    return _handle_response(response)


async def async_basic_auth_request(
    method: str,
    url: str,
    token: str = None,
    platform: SubscriptionPlatform = None,
    payload: Dict[str, Any] = None,
    params: Dict[str, Any] = None,
) -> RevenueCatResponse:
    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, **_build_request(token, platform, payload, params))

        return _handle_response(response)
