from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.receipts_body import ReceiptsBody
from ...types import Response


def _get_kwargs(
    *,
    body: ReceiptsBody,
    x_platform: str = "ios",
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["X-Platform"] = x_platform

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/receipts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReceiptsBody,
    x_platform: str = "ios",
) -> Response[Any]:
    """Create a Purchase

     Records a purchase for a user from iOS, Android, or Stripe and will create a user if they don't
    already exist.

    Args:
        x_platform (str):  Default: 'ios'.
        body (ReceiptsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        x_platform=x_platform,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ReceiptsBody,
    x_platform: str = "ios",
) -> Response[Any]:
    """Create a Purchase

     Records a purchase for a user from iOS, Android, or Stripe and will create a user if they don't
    already exist.

    Args:
        x_platform (str):  Default: 'ios'.
        body (ReceiptsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        x_platform=x_platform,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
