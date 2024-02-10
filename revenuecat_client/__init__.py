""" A client library for accessing RevenueCat API v1 """

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
