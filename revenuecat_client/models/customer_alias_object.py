from enum import Enum


class CustomerAliasObject(str, Enum):
    CUSTOMER_ALIAS = "customer.alias"

    def __str__(self) -> str:
        return str(self.value)
