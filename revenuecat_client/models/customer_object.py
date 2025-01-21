from enum import Enum


class CustomerObject(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
