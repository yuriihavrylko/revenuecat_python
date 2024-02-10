from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_non_subscriptions_onetime_item import (
        SubscriberSubscriberNonSubscriptionsOnetimeItem,
    )


T = TypeVar("T", bound="SubscriberSubscriberNonSubscriptions")


@_attrs_define
class SubscriberSubscriberNonSubscriptions:
    """
    Attributes:
        onetime (Union[Unset, List['SubscriberSubscriberNonSubscriptionsOnetimeItem']]):
    """

    onetime: Union[
        Unset, List["SubscriberSubscriberNonSubscriptionsOnetimeItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        onetime: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.onetime, Unset):
            onetime = []
            for onetime_item_data in self.onetime:
                onetime_item = onetime_item_data.to_dict()
                onetime.append(onetime_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if onetime is not UNSET:
            field_dict["onetime"] = onetime

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscriber_subscriber_non_subscriptions_onetime_item import (
            SubscriberSubscriberNonSubscriptionsOnetimeItem,
        )

        d = src_dict.copy()
        onetime = []
        _onetime = d.pop("onetime", UNSET)
        for onetime_item_data in _onetime or []:
            onetime_item = SubscriberSubscriberNonSubscriptionsOnetimeItem.from_dict(
                onetime_item_data
            )

            onetime.append(onetime_item)

        subscriber_subscriber_non_subscriptions = cls(
            onetime=onetime,
        )

        subscriber_subscriber_non_subscriptions.additional_properties = d
        return subscriber_subscriber_non_subscriptions

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
