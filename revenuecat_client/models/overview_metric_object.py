from enum import Enum


class OverviewMetricObject(str, Enum):
    OVERVIEW_METRIC = "overview_metric"

    def __str__(self) -> str:
        return str(self.value)
