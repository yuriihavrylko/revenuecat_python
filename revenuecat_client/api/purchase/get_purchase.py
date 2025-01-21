from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.purchase import Purchase
from ...types import Response


def _get_kwargs(
    project_id: str,
    purchase_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/purchases/{purchase_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Purchase]]:
    if response.status_code == 200:
        response_200 = Purchase.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Purchase]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Purchase]]:
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Purchase]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    purchase_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Purchase]]:
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Purchase]
    """

    return sync_detailed(
        project_id=project_id,
        purchase_id=purchase_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    purchase_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Purchase]]:
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Purchase]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        purchase_id=purchase_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    purchase_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Purchase]]:
    """Get a purchase

     This endpoint requires the following permission(s):
    <code>customer_information:purchases:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        purchase_id (str):  Example: purc1a2b3c4d5e.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Purchase]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            purchase_id=purchase_id,
            client=client,
        )
    ).parsed
