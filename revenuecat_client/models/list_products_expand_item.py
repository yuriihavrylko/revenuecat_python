from enum import Enum


class ListProductsExpandItem(str, Enum):
    ITEMS_APP = "items.app"

    def __str__(self) -> str:
        return str(self.value)
