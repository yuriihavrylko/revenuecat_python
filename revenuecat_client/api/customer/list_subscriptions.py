from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_subscriptions_environment import ListSubscriptionsEnvironment
from ...models.subscription_list import SubscriptionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    customer_id: str,
    *,
    environment: Union[Unset, ListSubscriptionsEnvironment] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_environment: Union[Unset, str] = UNSET
    if not isinstance(environment, Unset):
        json_environment = environment.value

    params["environment"] = json_environment

    params["starting_after"] = starting_after

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/customers/{customer_id}/subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SubscriptionList]]:
    if response.status_code == 200:
        response_200 = SubscriptionList.from_dict(response.json())

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
) -> Response[Union[Any, SubscriptionList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    environment: Union[Unset, ListSubscriptionsEnvironment] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[Union[Any, SubscriptionList]]:
    """Get a list of subscriptions associated with a customer

     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        environment (Union[Unset, ListSubscriptionsEnvironment]):
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SubscriptionList]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        environment=environment,
        starting_after=starting_after,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    environment: Union[Unset, ListSubscriptionsEnvironment] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[Any, SubscriptionList]]:
    """Get a list of subscriptions associated with a customer

     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        environment (Union[Unset, ListSubscriptionsEnvironment]):
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SubscriptionList]
    """

    return sync_detailed(
        project_id=project_id,
        customer_id=customer_id,
        client=client,
        environment=environment,
        starting_after=starting_after,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    environment: Union[Unset, ListSubscriptionsEnvironment] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[Union[Any, SubscriptionList]]:
    """Get a list of subscriptions associated with a customer

     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        environment (Union[Unset, ListSubscriptionsEnvironment]):
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SubscriptionList]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        customer_id=customer_id,
        environment=environment,
        starting_after=starting_after,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    environment: Union[Unset, ListSubscriptionsEnvironment] = UNSET,
    starting_after: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[Any, SubscriptionList]]:
    """Get a list of subscriptions associated with a customer

     This endpoint requires the following permission(s):
    <code>customer_information:subscriptions:read</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        customer_id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        environment (Union[Unset, ListSubscriptionsEnvironment]):
        starting_after (Union[Unset, str]):  Example: ent12354.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SubscriptionList]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            customer_id=customer_id,
            client=client,
            environment=environment,
            starting_after=starting_after,
            limit=limit,
        )
    ).parsed
