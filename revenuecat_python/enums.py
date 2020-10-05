from enum import Enum


class SubscriptionPlatform(Enum):
    ios = 'ios'
    android = 'android'
    macos = 'macos'
    uikitformac = 'uikitformac'
    stripe = 'stripe'


class AttributionNetworkCode(Enum):
    apple_search_ads = 0
    adjust = 1
    apps_flyer = 2
    branch = 3
    tenjin = 4
    facebook = 5