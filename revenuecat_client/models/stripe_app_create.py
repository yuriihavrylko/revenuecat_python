from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stripe_app_create_stripe import StripeAppCreateStripe


T = TypeVar("T", bound="StripeAppCreate")


@_attrs_define
class StripeAppCreate:
    """
    Attributes:
        stripe (Union[Unset, StripeAppCreateStripe]): Stripe type details. Should only be used when type is stripe.
    """

    stripe: Union[Unset, "StripeAppCreateStripe"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stripe, Unset):
            stripe = self.stripe.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe is not UNSET:
            field_dict["stripe"] = stripe

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stripe_app_create_stripe import StripeAppCreateStripe

        d = src_dict.copy()
        _stripe = d.pop("stripe", UNSET)
        stripe: Union[Unset, StripeAppCreateStripe]
        if isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = StripeAppCreateStripe.from_dict(_stripe)

        stripe_app_create = cls(
            stripe=stripe,
        )

        stripe_app_create.additional_properties = d
        return stripe_app_create

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
