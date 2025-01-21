from enum import Enum


class PurchaseObject(str, Enum):
    PURCHASE = "purchase"

    def __str__(self) -> str:
        return str(self.value)
