from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invoice_object import InvoiceObject

if TYPE_CHECKING:
    from ..models.invoice_line_item import InvoiceLineItem
    from ..models.monetary_amount import MonetaryAmount


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        object_ (InvoiceObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the invoice Example: rcbin1a2b3c4d5e.
        total_amount (MonetaryAmount):
        line_items (List['InvoiceLineItem']): List of line items that are part of the invoice. Each line item represents
            a product that was purchased.
        issued_at (int): The date when the invoiced was issued in ms since epoch Example: 1658399423658.
        paid_at (Union[None, int]): The date when the invoiced was paid in ms since epoch Example: 1658399423658.
        invoice_url (Union[None, str]): URL to download the invoice pdf Example:
            https://api.revenuecat.com/v2/projects/proj1ab2c3d4/customers/cust1ab2c3d4/invoices/inv1ab2c3d4/file.
    """

    object_: InvoiceObject
    id: str
    total_amount: "MonetaryAmount"
    line_items: List["InvoiceLineItem"]
    issued_at: int
    paid_at: Union[None, int]
    invoice_url: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        total_amount = self.total_amount.to_dict()

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        issued_at = self.issued_at

        paid_at: Union[None, int]
        paid_at = self.paid_at

        invoice_url: Union[None, str]
        invoice_url = self.invoice_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "total_amount": total_amount,
                "line_items": line_items,
                "issued_at": issued_at,
                "paid_at": paid_at,
                "invoice_url": invoice_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_line_item import InvoiceLineItem
        from ..models.monetary_amount import MonetaryAmount

        d = src_dict.copy()
        object_ = InvoiceObject(d.pop("object"))

        id = d.pop("id")

        total_amount = MonetaryAmount.from_dict(d.pop("total_amount"))

        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in _line_items:
            line_items_item = InvoiceLineItem.from_dict(line_items_item_data)

            line_items.append(line_items_item)

        issued_at = d.pop("issued_at")

        def _parse_paid_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        paid_at = _parse_paid_at(d.pop("paid_at"))

        def _parse_invoice_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        invoice_url = _parse_invoice_url(d.pop("invoice_url"))

        invoice = cls(
            object_=object_,
            id=id,
            total_amount=total_amount,
            line_items=line_items,
            issued_at=issued_at,
            paid_at=paid_at,
            invoice_url=invoice_url,
        )

        invoice.additional_properties = d
        return invoice

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
