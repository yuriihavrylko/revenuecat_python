from enum import Enum


class GetOfferingExpandItem(str, Enum):
    PACKAGE = "package"
    PACKAGE_PRODUCT = "package.product"

    def __str__(self) -> str:
        return str(self.value)
