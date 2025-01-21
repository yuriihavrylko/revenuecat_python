from enum import Enum


class GetEntitlementExpandItem(str, Enum):
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
