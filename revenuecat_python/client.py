from typing import Dict, Any

from .constants import (API_ROOT, SUBSCRIBER_ATTRIBUTES_PATH, PURCHASE_PATH, SUBSCRIBERS_PATH,
                        GRANT_PROMOTIONAL_ENTITLEMENT_PATH, REVOKE_PROMOTIONAL_ENTITLEMENT_PATH,
                        ADD_USER_ATTRIBUTION_PATH, DEFER_GOOGLE_SUBSCRIPTION_PATH,
                        DELETE_CURRENT_OFFERING_OVERRIDE_PATH,
                        OVERRIDE_CURRENT_OFFERING_PATH, REFUND_GOOGLE_SUBSCRIPTION_PATH)
from .decorators import require_secret
from .http_client import basic_auth_request, async_basic_auth_request
from .responses import RevenueCatResponse
from .enums import SubscriptionPlatform, AttributionNetworkCode


class BaseClient:
    def __init__(self, api_key: str, secret_key: str = None):
        self.api_key = api_key
        self.secret_key = secret_key

    def _get_path(self, path_name: str, **kwargs) -> str:
        return API_ROOT + path_name.format(**kwargs)

    def _kwargs_get_or_create_subscriber(self, app_user_id: str, get_attributes: bool = False, platform: SubscriptionPlatform = None) -> Dict[
        str, Any]:
        return {
            'method': 'GET',
            'url': self._get_path(SUBSCRIBERS_PATH, id=app_user_id),
            'token': self.secret_key if get_attributes else self.api_key,
            'platform': platform
        }

    def _kwargs_update_subscriber_attributes(self, app_user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(SUBSCRIBER_ATTRIBUTES_PATH, id=app_user_id),
            'token': self.api_key,
            'payload': data
        }

    def _kwargs_delete_subscriber(self, app_user_id: str) -> Dict[str, Any]:
        return {
            'method': 'DELETE',
            'url': self._get_path(SUBSCRIBERS_PATH, id=app_user_id),
            'token': self.secret_key
        }

    def _kwargs_create_purchase(self, data: Dict[str, Any], platform: SubscriptionPlatform) -> \
            Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(PURCHASE_PATH),
            'token': self.api_key,
            'payload': data,
            'platform': platform
        }

    def _kwargs_grant_promotional_entitlement(self, app_user_id: str, entitlement_id: str, data: Dict[str, Any]) -> \
            Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(GRANT_PROMOTIONAL_ENTITLEMENT_PATH, id=app_user_id, entitlement_id=entitlement_id),
            'token': self.secret_key,
            'payload': data,
        }

    def _kwargs_revoke_promotional_entitlement(self, app_user_id: str, entitlement_id: str) -> Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(REVOKE_PROMOTIONAL_ENTITLEMENT_PATH, id=app_user_id, entitlement_id=entitlement_id),
            'token': self.secret_key,
        }

    def _kwargs_refund_google_subscription(self, app_user_id: str, product_id: str) -> Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(REFUND_GOOGLE_SUBSCRIPTION_PATH, id=app_user_id, product_id=product_id),
            'token': self.secret_key,
        }

    def _kwargs_defer_google_subscription(self, app_user_id: str, product_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(DEFER_GOOGLE_SUBSCRIPTION_PATH, id=app_user_id, product_id=product_id),
            'token': self.secret_key,
            'payload': data
        }

    def _kwargs_add_user_attribution(self, app_user_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(ADD_USER_ATTRIBUTION_PATH, id=app_user_id),
            'token': self.api_key,
            'payload': data
        }

    def _kwargs_override_current_offering(self, app_user_id: str, offering_uuid: str) -> Dict[str, Any]:
        return {
            'method': 'POST',
            'url': self._get_path(OVERRIDE_CURRENT_OFFERING_PATH, id=app_user_id, offering_uuid=offering_uuid),
            'token': self.secret_key
        }

    def _kwargs_delete_current_offering_override(self, app_user_id: str) -> Dict[str, Any]:
        return {
            'method': 'DELETE',
            'url': self._get_path(DELETE_CURRENT_OFFERING_OVERRIDE_PATH, id=app_user_id),
            'token': self.secret_key
        }


class RevenueCatClient(BaseClient):
    def get_or_create_subscriber(self, app_user_id: str, get_attributes: bool = False, platform: SubscriptionPlatform = None) -> RevenueCatResponse:
        """
        Gets the latest subscriber info or creates one if it doesn't exist
        A new subscriber will be created with the app_user_id
        Reference: https://docs.revenuecat.com/reference#subscribers

        :param app_user_id: The app_user_id used with the mobile SDK
        :param get_attributes: User secret key to get additional field
        :param platform: Set platform to update the subscriber record's
        :return: Http response of RevenueCat
        """
        if platform:
            get_attributes = False

        return basic_auth_request(**self._kwargs_get_or_create_subscriber(app_user_id, get_attributes, platform))

    def update_subscriber_attributes(self, app_user_id: str, attributes: Dict[str, Any]) -> RevenueCatResponse:
        """
        Updates subscriber attributes for a user
        Reference: https://docs.revenuecat.com/reference#update-subscriber-attributes

        attributes = {
            "key_name_1": {
                "value": "custom_value_1",
                "updated_at_ms": 1606451476084,
            }
        }

        :param app_user_id: The app_user_id used with the mobile SDK
        :param attributes: Mapping of user's attributes
        :return: Http response of RevenueCat
        """
        data = {key: {'value': value} for key, value in attributes.items()}
        data = {'attributes': data}
        return basic_auth_request(**self._kwargs_update_subscriber_attributes(app_user_id, data))

    @require_secret()
    def delete_subscriber(self, app_user_id: str) -> RevenueCatResponse:
        """
        Permanently deletes a subscriber
        Reference: https://docs.revenuecat.com/reference#subscribersapp_user_id

        :param app_user_id: The app_user_id used with the mobile SDK
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_delete_subscriber(app_user_id))

    def create_purchase(self, app_user_id: str, data: Dict[str, Any],
                        platform: SubscriptionPlatform) -> RevenueCatResponse:
        """
        Permanently deletes a subscriber
        Reference: https://docs.revenuecat.com/reference#receipts

        :param app_user_id: The app_user_id used with the mobile SDK
        :param data: Purchase details
        :param platform: The platform this purchase is for
        :return: Http response of RevenueCat
        """
        data['app_user_id'] = app_user_id
        return basic_auth_request(**self._kwargs_create_purchase(data, platform))

    @require_secret()
    def grant_promotional_entitlement(self, app_user_id: str, entitlement_id: str,
                                      data: Dict[str, Any]) -> RevenueCatResponse:
        """
        Grants a user a promotional entitlement
        Reference: https://docs.revenuecat.com/reference#grant-a-promotional-entitlement

        :param app_user_id: The app_user_id used with the mobile SDK
        :param entitlement_id: The identifier for the entitlement you want to grant to the user
        :param data: Duration and start time
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_grant_promotional_entitlement(app_user_id, entitlement_id, data))

    @require_secret()
    def revoke_promotional_entitlement(self, app_user_id: str, entitlement_id: str) -> RevenueCatResponse:
        """
        Revokes all promotional entitlements for a given entitlement identifier and app user ID
        Reference: https://docs.revenuecat.com/reference#revoke-promotional-entitlements

        :param app_user_id: The app_user_id used with the mobile SDK
        :param entitlement_id: The identifier for the entitlement you want to grant to the user
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_revoke_promotional_entitlement(app_user_id, entitlement_id))

    @require_secret()
    def refund_google_subscription(self, app_user_id: str, product_id: str) -> RevenueCatResponse:
        """
        Immediately revokes access to a Google Subscription and issues a refund for the last purchase
        Reference: https://docs.revenuecat.com/reference#revoke-a-google-subscription

        :param app_user_id: The app_user_id used with the mobile SDK
        :param product_id: The identifier of the product belonging to the subscription that is being revoked
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_refund_google_subscription(app_user_id, product_id))

    @require_secret()
    def defer_google_subscription(self, app_user_id: str, product_id: str, data: Dict[str, Any]) -> RevenueCatResponse:
        """
        Defers the purchase of a Google Subscription to a later date
        Reference: https://docs.revenuecat.com/reference#defer-a-google-subscription

        :param app_user_id: The app_user_id used with the mobile SDK
        :param product_id: The identifier of the product belonging to the subscription that is being revoked
        :param data: The desired next expiry time to assign to the subscription
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_defer_google_subscription(app_user_id, product_id, data))

    def add_user_attribution(self, app_user_id: str, data: Dict[str, Any], network: AttributionNetworkCode) -> RevenueCatResponse:
        """
        Attaches attribution data to a subscriber from specific supported networks
        Reference: https://docs.revenuecat.com/reference#subscribersattribution

        :param app_user_id: The app_user_id used with the mobile SDK
        :param data: The data returned by the attribution network callbacks
        :param network: Network code
        :return: Http response of RevenueCat
        """
        data = {'data': data, 'network': network.value}
        return basic_auth_request(**self._kwargs_add_user_attribution(app_user_id, data))

    @require_secret()
    def override_current_offering(self, app_user_id: str, offering_uuid: str) -> RevenueCatResponse:
        """
        Overrides the current Offering for a specific user
        Reference: https://docs.revenuecat.com/reference#override-offering

        :param app_user_id: The app_user_id used with the mobile SDK
        :param offering_uuid: The UUID for the offering you want to set as the override for the user
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_override_current_offering(app_user_id, offering_uuid))

    @require_secret()
    def delete_current_offering_override(self, app_user_id: str) -> RevenueCatResponse:
        """
        Reset the offering overrides back to the current offering for a specific user
        Reference: https://docs.revenuecat.com/reference#delete-offering-override

        :param app_user_id: The app_user_id used with the mobile SDK
        :return: Http response of RevenueCat
        """
        return basic_auth_request(**self._kwargs_delete_current_offering_override(app_user_id))


class AsyncRevenueCatClient(BaseClient):
    async def get_or_create_subscriber(self, app_user_id: str, get_attributes: bool = False, platform: SubscriptionPlatform = None) -> RevenueCatResponse:
        """
        Gets the latest subscriber info or creates one if it doesn't exist
        A new subscriber will be created with the app_user_id
        Reference: https://docs.revenuecat.com/reference#subscribers

        :param app_user_id: The app_user_id used with the mobile SDK
        :param get_attributes: User secret key to get additional field
        :param platform: Set platform to update the subscriber record's
        :return: Http response of RevenueCat
        """
        if platform:
            get_attributes = False

        return await async_basic_auth_request(**self._kwargs_get_or_create_subscriber(app_user_id, get_attributes, platform))

    async def update_subscriber_attributes(self, app_user_id: str, attributes: Dict[str, Any]) -> RevenueCatResponse:
        """
        Updates subscriber attributes for a user
        Reference: https://docs.revenuecat.com/reference#update-subscriber-attributes

        attributes = {
            "key_name_1": {
                "value": "custom_value_1",
                "updated_at_ms": 1606451476084,
            }
        }

        :param app_user_id: The app_user_id used with the mobile SDK
        :param attributes: Mapping of user's attributes
        :return: Http response of RevenueCat
        """
        data = {key: {'value': value} for key, value in attributes.items()}
        data = {'attributes': data}
        return await async_basic_auth_request(**self._kwargs_update_subscriber_attributes(app_user_id, data))

    @require_secret()
    async def delete_subscriber(self, app_user_id: str) -> RevenueCatResponse:
        """
        Permanently deletes a subscriber
        Reference: https://docs.revenuecat.com/reference#subscribersapp_user_id

        :param app_user_id: The app_user_id used with the mobile SDK
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_delete_subscriber(app_user_id))

    async def create_purchase(self, app_user_id: str, data: Dict[str, Any],
                        platform: SubscriptionPlatform) -> RevenueCatResponse:
        """
        Permanently deletes a subscriber
        Reference: https://docs.revenuecat.com/reference#receipts

        :param app_user_id: The app_user_id used with the mobile SDK
        :param data: Purchase details
        :param platform: The platform this purchase is for
        :return: Http response of RevenueCat
        """
        data['app_user_id'] = app_user_id
        return await async_basic_auth_request(**self._kwargs_create_purchase(data, platform))

    @require_secret()
    async def grant_promotional_entitlement(self, app_user_id: str, entitlement_id: str,
                                      data: Dict[str, Any]) -> RevenueCatResponse:
        """
        Grants a user a promotional entitlement
        Reference: https://docs.revenuecat.com/reference#grant-a-promotional-entitlement

        :param app_user_id: The app_user_id used with the mobile SDK
        :param entitlement_id: The identifier for the entitlement you want to grant to the user
        :param data: Duration and start time
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_grant_promotional_entitlement(app_user_id, entitlement_id, data))

    @require_secret()
    async def revoke_promotional_entitlement(self, app_user_id: str, entitlement_id: str) -> RevenueCatResponse:
        """
        Revokes all promotional entitlements for a given entitlement identifier and app user ID
        Reference: https://docs.revenuecat.com/reference#revoke-promotional-entitlements

        :param app_user_id: The app_user_id used with the mobile SDK
        :param entitlement_id: The identifier for the entitlement you want to grant to the user
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_revoke_promotional_entitlement(app_user_id, entitlement_id))

    @require_secret()
    async def refund_google_subscription(self, app_user_id: str, product_id: str) -> RevenueCatResponse:
        """
        Immediately revokes access to a Google Subscription and issues a refund for the last purchase
        Reference: https://docs.revenuecat.com/reference#revoke-a-google-subscription

        :param app_user_id: The app_user_id used with the mobile SDK
        :param product_id: The identifier of the product belonging to the subscription that is being revoked
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_refund_google_subscription(app_user_id, product_id))

    @require_secret()
    async def defer_google_subscription(self, app_user_id: str, product_id: str, data: Dict[str, Any]) -> RevenueCatResponse:
        """
        Defers the purchase of a Google Subscription to a later date
        Reference: https://docs.revenuecat.com/reference#defer-a-google-subscription

        :param app_user_id: The app_user_id used with the mobile SDK
        :param product_id: The identifier of the product belonging to the subscription that is being revoked
        :param data: The desired next expiry time to assign to the subscription
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_defer_google_subscription(app_user_id, product_id, data))

    async def add_user_attribution(self, app_user_id: str, data: Dict[str, Any], network: AttributionNetworkCode) -> RevenueCatResponse:
        """
        Attaches attribution data to a subscriber from specific supported networks
        Reference: https://docs.revenuecat.com/reference#subscribersattribution

        :param app_user_id: The app_user_id used with the mobile SDK
        :param data: The data returned by the attribution network callbacks
        :param network: Network code
        :return: Http response of RevenueCat
        """
        data = {'data': data, 'network': network.value}
        return await async_basic_auth_request(**self._kwargs_add_user_attribution(app_user_id, data))

    @require_secret()
    async def override_current_offering(self, app_user_id: str, offering_uuid: str) -> RevenueCatResponse:
        """
        Overrides the current Offering for a specific user
        Reference: https://docs.revenuecat.com/reference#override-offering

        :param app_user_id: The app_user_id used with the mobile SDK
        :param offering_uuid: The UUID for the offering you want to set as the override for the user
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_override_current_offering(app_user_id, offering_uuid))

    @require_secret()
    async def delete_current_offering_override(self, app_user_id: str) -> RevenueCatResponse:
        """
        Reset the offering overrides back to the current offering for a specific user
        Reference: https://docs.revenuecat.com/reference#delete-offering-override

        :param app_user_id: The app_user_id used with the mobile SDK
        :return: Http response of RevenueCat
        """
        return await async_basic_auth_request(**self._kwargs_delete_current_offering_override(app_user_id))
