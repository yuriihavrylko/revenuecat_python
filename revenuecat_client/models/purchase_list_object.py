from enum import Enum


class PurchaseListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
