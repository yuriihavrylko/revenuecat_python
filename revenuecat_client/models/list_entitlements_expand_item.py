from enum import Enum


class ListEntitlementsExpandItem(str, Enum):
    ITEMS_PRODUCT = "items.product"

    def __str__(self) -> str:
        return str(self.value)
