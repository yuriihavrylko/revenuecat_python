from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppBodyStripe")


@_attrs_define
class UpdateAppBodyStripe:
    """Stripe type details. Should only be used when type is stripe.

    Attributes:
        stripe_account_id (Union[Unset, str]): It needs to be connected to your RevenueCat account. It can be omitted if
            you only have a single Stripe account connected to your RevenueCat account.
    """

    stripe_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe_account_id = self.stripe_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe_account_id is not UNSET:
            field_dict["stripe_account_id"] = stripe_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stripe_account_id = d.pop("stripe_account_id", UNSET)

        update_app_body_stripe = cls(
            stripe_account_id=stripe_account_id,
        )

        update_app_body_stripe.additional_properties = d
        return update_app_body_stripe

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
