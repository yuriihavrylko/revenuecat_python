from enum import Enum


class PackageObject(str, Enum):
    PACKAGE = "package"

    def __str__(self) -> str:
        return str(self.value)
