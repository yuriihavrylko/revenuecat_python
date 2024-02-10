from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.subscriber import Subscriber
from ...types import Response, Unset


def _get_kwargs(
    app_user_id: str,
    *,
    x_platform: Union[Unset, str] = "ios",
    x_is_sandbox: Union[Unset, str] = "false",
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_platform, Unset):
        headers["X-Platform"] = x_platform

    if not isinstance(x_is_sandbox, Unset):
        headers["X-Is-Sandbox"] = x_is_sandbox

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/subscribers/{app_user_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Subscriber]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Subscriber.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Subscriber]]:
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
    x_platform: Union[Unset, str] = "ios",
    x_is_sandbox: Union[Unset, str] = "false",
) -> Response[Union[Any, Subscriber]]:
    """Get or Create Subscriber

     Gets the latest subscriber info or creates one if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (Union[Unset, str]):  Default: 'ios'.
        x_is_sandbox (Union[Unset, str]):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Subscriber]]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        x_platform=x_platform,
        x_is_sandbox=x_is_sandbox,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: Union[Unset, str] = "ios",
    x_is_sandbox: Union[Unset, str] = "false",
) -> Optional[Union[Any, Subscriber]]:
    """Get or Create Subscriber

     Gets the latest subscriber info or creates one if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (Union[Unset, str]):  Default: 'ios'.
        x_is_sandbox (Union[Unset, str]):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Subscriber]
    """

    return sync_detailed(
        app_user_id=app_user_id,
        client=client,
        x_platform=x_platform,
        x_is_sandbox=x_is_sandbox,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: Union[Unset, str] = "ios",
    x_is_sandbox: Union[Unset, str] = "false",
) -> Response[Union[Any, Subscriber]]:
    """Get or Create Subscriber

     Gets the latest subscriber info or creates one if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (Union[Unset, str]):  Default: 'ios'.
        x_is_sandbox (Union[Unset, str]):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Subscriber]]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        x_platform=x_platform,
        x_is_sandbox=x_is_sandbox,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_platform: Union[Unset, str] = "ios",
    x_is_sandbox: Union[Unset, str] = "false",
) -> Optional[Union[Any, Subscriber]]:
    """Get or Create Subscriber

     Gets the latest subscriber info or creates one if it doesn't exist.

    Args:
        app_user_id (str):
        x_platform (Union[Unset, str]):  Default: 'ios'.
        x_is_sandbox (Union[Unset, str]):  Default: 'false'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Subscriber]
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
            x_platform=x_platform,
            x_is_sandbox=x_is_sandbox,
        )
    ).parsed
