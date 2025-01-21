from enum import Enum


class GetPackageExpandItem(str, Enum):
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
