from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_offerings_response_200 import GetOfferingsResponse200
from ...models.get_offerings_response_400 import GetOfferingsResponse400
from ...models.get_offerings_response_403 import GetOfferingsResponse403
from ...types import Response


def _get_kwargs(
    app_user_id: str,
    *,
    x_platform: str = "ios",
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["X-Platform"] = x_platform

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/subscribers/{app_user_id}/offerings",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetOfferingsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetOfferingsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GetOfferingsResponse403.from_dict(response.json())

        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: str = "ios",
) -> Response[
    Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
]:
    """Get Offerings

     Gets the offerings for your app.

    Args:
        app_user_id (str):
        x_platform (str):  Default: 'ios'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        x_platform=x_platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: str = "ios",
) -> Optional[
    Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
]:
    """Get Offerings

     Gets the offerings for your app.

    Args:
        app_user_id (str):
        x_platform (str):  Default: 'ios'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
    """

    return sync_detailed(
        app_user_id=app_user_id,
        client=client,
        x_platform=x_platform,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: str = "ios",
) -> Response[
    Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
]:
    """Get Offerings

     Gets the offerings for your app.

    Args:
        app_user_id (str):
        x_platform (str):  Default: 'ios'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        x_platform=x_platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: str = "ios",
) -> Optional[
    Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
]:
    """Get Offerings

     Gets the offerings for your app.

    Args:
        app_user_id (str):
        x_platform (str):  Default: 'ios'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOfferingsResponse200, GetOfferingsResponse400, GetOfferingsResponse403]
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
            x_platform=x_platform,
        )
    ).parsed
