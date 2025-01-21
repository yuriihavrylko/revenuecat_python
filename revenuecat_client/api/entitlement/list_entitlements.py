from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entitlement_list import EntitlementList
from ...models.list_entitlements_expand_item import ListEntitlementsExpandItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    expand: Union[Unset, List[ListEntitlementsExpandItem]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["starting_after"] = starting_after

    params["limit"] = limit

    json_expand: Union[Unset, List[str]] = UNSET
    if not isinstance(expand, Unset):
        json_expand = []
        for expand_item_data in expand:
            expand_item = expand_item_data.value
            json_expand.append(expand_item)

    params["expand"] = json_expand

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/entitlements",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EntitlementList]]:
    if response.status_code == 200:
        response_200 = EntitlementList.from_dict(response.json())

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
) -> Response[Union[Any, EntitlementList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    expand: Union[Unset, List[ListEntitlementsExpandItem]] = UNSET,
) -> Response[Union[Any, EntitlementList]]:
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.
        expand (Union[Unset, List[ListEntitlementsExpandItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntitlementList]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    expand: Union[Unset, List[ListEntitlementsExpandItem]] = UNSET,
) -> Optional[Union[Any, EntitlementList]]:
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.
        expand (Union[Unset, List[ListEntitlementsExpandItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EntitlementList]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    expand: Union[Unset, List[ListEntitlementsExpandItem]] = UNSET,
) -> Response[Union[Any, EntitlementList]]:
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.
        expand (Union[Unset, List[ListEntitlementsExpandItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntitlementList]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        starting_after=starting_after,
        limit=limit,
        expand=expand,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    expand: Union[Unset, List[ListEntitlementsExpandItem]] = UNSET,
) -> Optional[Union[Any, EntitlementList]]:
    """Get a list of entitlements

     This endpoint requires the following permission(s):
    <code>project_configuration:entitlements:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.
        expand (Union[Unset, List[ListEntitlementsExpandItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EntitlementList]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            starting_after=starting_after,
            limit=limit,
            expand=expand,
        )
    ).parsed
