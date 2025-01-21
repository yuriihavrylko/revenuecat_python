from enum import Enum


class CustomerActiveEntitlementListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
