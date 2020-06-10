from enum import Enum

from .constants import ENDPOINTS
from .decorators import require_secret
from .request import basic_auth_request


class SubscriptionPlatform(Enum):
    ios = 'ios'
    android = 'android'
    macos = 'macos'
    uikitformac = 'uikitformac'
    stripe = 'stripe'


class RevenueCatClient:
    def __init__(self, api_key: str, secret_key: str = None):
        self.api_key = api_key
        self.secret_key = secret_key

    def _get_path(self, path_name: str, **kwargs) -> str:
        return ENDPOINTS['API_ROOT'] + ENDPOINTS[path_name].format(**kwargs)

    def get_or_create_subscriber(self, app_user_id: str, platform: SubscriptionPlatform = None) -> dict:
        url = self._get_path('SUBSCRIBERS_PATH', id=app_user_id)
        result = basic_auth_request('GET', url, token=self.secret_key or self.api_key, platform=platform)
        return result['subscriber']

    @require_secret()
    def delete_subscriber(self, app_user_id: str) -> bool:
        url = self._get_path('SUBSCRIBERS_PATH', id=app_user_id)
        result = basic_auth_request('DELETE', url, token=self.secret_key)
        return result['deleted']

    def update_subscriber_attributes(self, app_user_id: str, data: dict) -> bool:
        url = self._get_path('SUBSCRIBER_ATTRIBUTES_PATH', id=app_user_id)

        data = {key: {'value': value} for key, value in data.items()}
        result = basic_auth_request('POST', url, token=self.api_key, payload={'attributes': data})
        return len(result) == 0

    def create_purchase(self, app_user_id: str, data: dict, platform: SubscriptionPlatform) -> dict:
        url = self._get_path('PURCHASE_PATH')
        data['app_user_id'] = app_user_id
        result = basic_auth_request('POST', url, token=self.api_key, payload=data, platform=platform)
        return result['subscriber']
