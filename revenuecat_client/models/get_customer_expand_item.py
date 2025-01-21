from enum import Enum


class GetCustomerExpandItem(str, Enum):
    ATTRIBUTES = "attributes"

    def __str__(self) -> str:
        return str(self.value)
