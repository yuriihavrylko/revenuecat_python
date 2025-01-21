from enum import Enum


class Ownership(str, Enum):
    FAMILY_SHARED = "family_shared"
    PURCHASED = "purchased"

    def __str__(self) -> str:
        return str(self.value)
