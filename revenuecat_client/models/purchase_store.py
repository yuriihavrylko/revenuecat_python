from enum import Enum


class PurchaseStore(str, Enum):
    AMAZON = "amazon"
    APP_STORE = "app_store"
    MAC_APP_STORE = "mac_app_store"
    PLAY_STORE = "play_store"
    PROMOTIONAL = "promotional"
    RC_BILLING = "rc_billing"
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
