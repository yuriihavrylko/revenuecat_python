from enum import Enum


class OverviewMetricPeriod(str, Enum):
    P0D = "P0D"
    P28D = "P28D"

    def __str__(self) -> str:
        return str(self.value)
