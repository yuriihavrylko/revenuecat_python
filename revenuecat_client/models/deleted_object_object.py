from enum import Enum


class DeletedObjectObject(str, Enum):
    APP = "app"
    CUSTOMER = "customer"
    ENTITLEMENT = "entitlement"
    OFFERING = "offering"
    PACKAGE = "package"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
