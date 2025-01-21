from enum import Enum


class CustomerAttributeListObject(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
