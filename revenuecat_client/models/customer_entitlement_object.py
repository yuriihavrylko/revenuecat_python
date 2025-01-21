from enum import Enum


class CustomerEntitlementObject(str, Enum):
    CUSTOMER_ACTIVE_ENTITLEMENT = "customer.active_entitlement"

    def __str__(self) -> str:
        return str(self.value)
