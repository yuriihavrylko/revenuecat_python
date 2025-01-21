from enum import Enum


class OverviewMetricsObject(str, Enum):
    OVERVIEW_METRICS = "overview_metrics"

    def __str__(self) -> str:
        return str(self.value)
