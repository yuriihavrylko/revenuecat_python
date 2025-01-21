from enum import Enum


class InvoiceLineItemObject(str, Enum):
    INVOICE_LINE_ITEM = "invoice.line_item"

    def __str__(self) -> str:
        return str(self.value)
