from enum import Enum


class ProjectObject(str, Enum):
    PROJECT = "project"

    def __str__(self) -> str:
        return str(self.value)
