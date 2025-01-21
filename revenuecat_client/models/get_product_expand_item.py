from enum import Enum


class GetProductExpandItem(str, Enum):
    APP = "app"

    def __str__(self) -> str:
        return str(self.value)
