from enum import Enum


class ListPackagesExpandItem(str, Enum):
    ITEMS_PRODUCT = "items.product"

    def __str__(self) -> str:
        return str(self.value)
