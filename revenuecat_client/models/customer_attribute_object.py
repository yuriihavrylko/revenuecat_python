from enum import Enum


class CustomerAttributeObject(str, Enum):
    CUSTOMER_ATTRIBUTE = "customer.attribute"

    def __str__(self) -> str:
        return str(self.value)
