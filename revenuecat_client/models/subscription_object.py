from enum import Enum


class SubscriptionObject(str, Enum):
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
