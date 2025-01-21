from enum import Enum


class EligibilityCriteria(str, Enum):
    ALL = "all"
    GOOGLE_SDK_GE_6 = "google_sdk_ge_6"
    GOOGLE_SDK_LT_6 = "google_sdk_lt_6"

    def __str__(self) -> str:
        return str(self.value)
