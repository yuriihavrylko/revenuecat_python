from enum import Enum


class ExperimentEnrollmentType0Object(str, Enum):
    EXPERIMENT_ENROLLMENT = "experiment_enrollment"

    def __str__(self) -> str:
        return str(self.value)
