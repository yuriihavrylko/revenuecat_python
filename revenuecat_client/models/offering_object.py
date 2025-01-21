from enum import Enum


class OfferingObject(str, Enum):
    OFFERING = "offering"

    def __str__(self) -> str:
        return str(self.value)
