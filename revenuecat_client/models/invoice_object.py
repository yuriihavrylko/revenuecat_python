from enum import Enum


class InvoiceObject(str, Enum):
    INVOICE = "invoice"

    def __str__(self) -> str:
        return str(self.value)
