from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_subscriber_attributes_body import UpdateSubscriberAttributesBody
from ...models.update_subscriber_attributes_response_400 import (
    UpdateSubscriberAttributesResponse400,
)
from ...types import Response


def _get_kwargs(
    app_user_id: str,
    *,
    body: UpdateSubscriberAttributesBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/subscribers/{app_user_id}/attributes",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateSubscriberAttributesResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = UpdateSubscriberAttributesResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateSubscriberAttributesResponse400]]:
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
    body: UpdateSubscriberAttributesBody,
) -> Response[Union[Any, UpdateSubscriberAttributesResponse400]]:
    """Update Subscriber Attributes

     Updates subscriber attributes for a user.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateSubscriberAttributesResponse400]]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSubscriberAttributesBody,
) -> Optional[Union[Any, UpdateSubscriberAttributesResponse400]]:
    """Update Subscriber Attributes

     Updates subscriber attributes for a user.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateSubscriberAttributesResponse400]
    """

    return sync_detailed(
        app_user_id=app_user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSubscriberAttributesBody,
) -> Response[Union[Any, UpdateSubscriberAttributesResponse400]]:
    """Update Subscriber Attributes

     Updates subscriber attributes for a user.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateSubscriberAttributesResponse400]]
    """

    kwargs = _get_kwargs(
        app_user_id=app_user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    app_user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateSubscriberAttributesBody,
) -> Optional[Union[Any, UpdateSubscriberAttributesResponse400]]:
    """Update Subscriber Attributes

     Updates subscriber attributes for a user.

    Args:
        app_user_id (str):
        body (UpdateSubscriberAttributesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateSubscriberAttributesResponse400]
    """

    return (
        await asyncio_detailed(
            app_user_id=app_user_id,
            client=client,
            body=body,
        )
    ).parsed
