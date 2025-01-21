from enum import Enum


class ProductsFromEntitlementListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
