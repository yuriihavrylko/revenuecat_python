from enum import Enum


class AppCreateType(str, Enum):
    AMAZON = "amazon"
    APP_STORE = "app_store"
    MAC_APP_STORE = "mac_app_store"
    PLAY_STORE = "play_store"
    RC_BILLING = "rc_billing"
    ROKU = "roku"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
