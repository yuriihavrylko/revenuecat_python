from enum import Enum


class ListOfferingsExpandItem(str, Enum):
    ITEMS_PACKAGE = "items.package"
    ITEMS_PACKAGE_PRODUCT = "items.package.product"

    def __str__(self) -> str:
        return str(self.value)
