from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_entitlements_pro_cat import (
        SubscriberSubscriberEntitlementsProCat,
    )


T = TypeVar("T", bound="SubscriberSubscriberEntitlements")


@_attrs_define
class SubscriberSubscriberEntitlements:
    """
    Attributes:
        pro_cat (Union[Unset, SubscriberSubscriberEntitlementsProCat]):
    """

    pro_cat: Union[Unset, "SubscriberSubscriberEntitlementsProCat"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pro_cat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pro_cat, Unset):
            pro_cat = self.pro_cat.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pro_cat is not UNSET:
            field_dict["pro_cat"] = pro_cat

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscriber_subscriber_entitlements_pro_cat import (
            SubscriberSubscriberEntitlementsProCat,
        )

        d = src_dict.copy()
        _pro_cat = d.pop("pro_cat", UNSET)
        pro_cat: Union[Unset, SubscriberSubscriberEntitlementsProCat]
        if isinstance(_pro_cat, Unset):
            pro_cat = UNSET
        else:
            pro_cat = SubscriberSubscriberEntitlementsProCat.from_dict(_pro_cat)

        subscriber_subscriber_entitlements = cls(
            pro_cat=pro_cat,
        )

        subscriber_subscriber_entitlements.additional_properties = d
        return subscriber_subscriber_entitlements

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
