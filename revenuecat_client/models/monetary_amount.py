from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.currency import Currency
from ..types import UNSET, Unset

T = TypeVar("T", bound="MonetaryAmount")


@_attrs_define
class MonetaryAmount:
    """
    Attributes:
        currency (Currency): ISO 4217 currency code Example: USD.
        gross (float): Total revenue generated (excluding taxes and commission) Example: 9.99.
        tax (float): Estimated taxes deducted from gross revenue Example: 0.75.
        proceeds (float): Net revenue after store commission / fees and taxes Example: 6.25.
        commission (Union[Unset, float]): Store commission or payment processor fees deducted from gross revenue (if
            any) Example: 2.99.
    """

    currency: Currency
    gross: float
    tax: float
    proceeds: float
    commission: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency.value

        gross = self.gross

        tax = self.tax

        proceeds = self.proceeds

        commission = self.commission

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "gross": gross,
                "tax": tax,
                "proceeds": proceeds,
            }
        )
        if commission is not UNSET:
            field_dict["commission"] = commission

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = Currency(d.pop("currency"))

        gross = d.pop("gross")

        tax = d.pop("tax")

        proceeds = d.pop("proceeds")

        commission = d.pop("commission", UNSET)

        monetary_amount = cls(
            currency=currency,
            gross=gross,
            tax=tax,
            proceeds=proceeds,
            commission=commission,
        )

        monetary_amount.additional_properties = d
        return monetary_amount

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
