from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    app_user_id: str,
    store_transaction_identifier: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/subscribers/{app_user_id}/transactions/{store_transaction_identifier}/refund",
    }

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
    app_user_id: str,
    store_transaction_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Google Play: Refund and Revoke Purchase

     Issues a refund for the most recent purchase of a Google product and revokes access. Works for
    subscription and non-subscription purchases that occurred in the last 365 days.

    Args:
        app_user_id (str):
        store_transaction_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        store_transaction_identifier=store_transaction_identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    app_user_id: str,
    store_transaction_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Any]:
    """Google Play: Refund and Revoke Purchase

     Issues a refund for the most recent purchase of a Google product and revokes access. Works for
    subscription and non-subscription purchases that occurred in the last 365 days.

    Args:
        app_user_id (str):
        store_transaction_identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        store_transaction_identifier=store_transaction_identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
