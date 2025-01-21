from enum import Enum


class AppObject(str, Enum):
    APP = "app"

    def __str__(self) -> str:
        return str(self.value)
