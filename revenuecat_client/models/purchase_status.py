from enum import Enum


class PurchaseStatus(str, Enum):
    OWNED = "owned"
    REFUNDED = "refunded"

    def __str__(self) -> str:
        return str(self.value)
