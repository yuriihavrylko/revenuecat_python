from enum import Enum


class SubscriptionAutoRenewalStatus(str, Enum):
    HAS_ALREADY_RENEWED = "has_already_renewed"
    REQUIRES_PRICE_INCREASE_CONSENT = "requires_price_increase_consent"
    WILL_CHANGE_PRODUCT = "will_change_product"
    WILL_NOT_RENEW = "will_not_renew"
    WILL_PAUSE = "will_pause"
    WILL_RENEW = "will_renew"

    def __str__(self) -> str:
        return str(self.value)
