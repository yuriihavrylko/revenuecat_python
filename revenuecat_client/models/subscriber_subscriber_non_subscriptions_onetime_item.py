from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberSubscriberNonSubscriptionsOnetimeItem")


@_attrs_define
class SubscriberSubscriberNonSubscriptionsOnetimeItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: cadba0c81b.
        is_sandbox (Union[Unset, bool]):  Default: True. Example: True.
        purchase_date (Union[Unset, str]):  Example: 2019-04-05T21:52:45Z.
        store (Union[Unset, str]):  Example: app_store.
    """

    id: Union[Unset, str] = UNSET
    is_sandbox: Union[Unset, bool] = True
    purchase_date: Union[Unset, str] = UNSET
    store: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        is_sandbox = self.is_sandbox

        purchase_date = self.purchase_date

        store = self.store

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_sandbox is not UNSET:
            field_dict["is_sandbox"] = is_sandbox
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if store is not UNSET:
            field_dict["store"] = store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_sandbox = d.pop("is_sandbox", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        store = d.pop("store", UNSET)

        subscriber_subscriber_non_subscriptions_onetime_item = cls(
            id=id,
            is_sandbox=is_sandbox,
            purchase_date=purchase_date,
            store=store,
        )

        subscriber_subscriber_non_subscriptions_onetime_item.additional_properties = d
        return subscriber_subscriber_non_subscriptions_onetime_item

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
