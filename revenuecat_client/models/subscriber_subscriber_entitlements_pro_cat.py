from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberSubscriberEntitlementsProCat")


@_attrs_define
class SubscriberSubscriberEntitlementsProCat:
    """
    Attributes:
        expires_date (Union[Unset, Any]):
        grace_period_expires_date (Union[Unset, Any]):
        product_identifier (Union[Unset, str]):  Example: onetime.
        purchase_date (Union[Unset, str]):  Example: 2019-04-05T21:52:45Z.
    """

    expires_date: Union[Unset, Any] = UNSET
    grace_period_expires_date: Union[Unset, Any] = UNSET
    product_identifier: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expires_date = self.expires_date

        grace_period_expires_date = self.grace_period_expires_date

        product_identifier = self.product_identifier

        purchase_date = self.purchase_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_date is not UNSET:
            field_dict["expires_date"] = expires_date
        if grace_period_expires_date is not UNSET:
            field_dict["grace_period_expires_date"] = grace_period_expires_date
        if product_identifier is not UNSET:
            field_dict["product_identifier"] = product_identifier
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expires_date = d.pop("expires_date", UNSET)

        grace_period_expires_date = d.pop("grace_period_expires_date", UNSET)

        product_identifier = d.pop("product_identifier", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        subscriber_subscriber_entitlements_pro_cat = cls(
            expires_date=expires_date,
            grace_period_expires_date=grace_period_expires_date,
            product_identifier=product_identifier,
            purchase_date=purchase_date,
        )

        subscriber_subscriber_entitlements_pro_cat.additional_properties = d
        return subscriber_subscriber_entitlements_pro_cat

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
