from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_product_body import CreateProductBody
from ...models.product import Product
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreateProductBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/products",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Product]]:
    if response.status_code == 201:
        response_201 = Product.from_dict(response.json())

        return response_201
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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == 423:
        response_423 = cast(Any, None)
        return response_423
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
) -> Response[Union[Any, Product]]:
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
    body: CreateProductBody,
) -> Response[Union[Any, Product]]:
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create RevenueCat Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Product]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateProductBody,
) -> Optional[Union[Any, Product]]:
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create RevenueCat Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Product]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateProductBody,
) -> Response[Union[Any, Product]]:
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create RevenueCat Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Product]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateProductBody,
) -> Optional[Union[Any, Product]]:
    r"""Create a product

     <div class=\"theme-admonition theme-admonition-info alert alert--warning\">
      <div class=\"heading\">Warning</div>
      <div>This endpoint does not allow to create RevenueCat Billing products.</div>
    This endpoint requires the following permission(s):
    <code>project_configuration:products:read_write</code>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreateProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Product]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
