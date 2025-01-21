from enum import Enum


class ProductsFromPackageListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
