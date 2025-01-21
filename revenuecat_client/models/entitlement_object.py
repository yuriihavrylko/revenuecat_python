from enum import Enum


class EntitlementObject(str, Enum):
    ENTITLEMENT = "entitlement"

    def __str__(self) -> str:
        return str(self.value)
