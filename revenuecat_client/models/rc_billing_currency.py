from enum import Enum


class RCBillingCurrency(str, Enum):
    AUD = "AUD"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
