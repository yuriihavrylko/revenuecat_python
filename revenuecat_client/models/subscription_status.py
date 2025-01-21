from enum import Enum


class SubscriptionStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    INCOMPLETE = "incomplete"
    IN_BILLING_RETRY = "in_billing_retry"
    IN_GRACE_PERIOD = "in_grace_period"
    PAUSED = "paused"
    TRIALING = "trialing"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
