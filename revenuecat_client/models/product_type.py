from enum import Enum


class ProductType(str, Enum):
    ONE_TIME = "one_time"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
