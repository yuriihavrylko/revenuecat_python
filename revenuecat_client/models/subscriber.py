from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber import SubscriberSubscriber


T = TypeVar("T", bound="Subscriber")


@_attrs_define
class Subscriber:
    """
    Attributes:
        request_date (Union[Unset, str]):  Example: 2019-07-26T17:40:10Z.
        request_date_ms (Union[Unset, int]):  Default: 0. Example: 1564162810884.
        subscriber (Union[Unset, SubscriberSubscriber]):
    """

    request_date: Union[Unset, str] = UNSET
    request_date_ms: Union[Unset, int] = 0
    subscriber: Union[Unset, "SubscriberSubscriber"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_date = self.request_date

        request_date_ms = self.request_date_ms

        subscriber: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscriber, Unset):
            subscriber = self.subscriber.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_date is not UNSET:
            field_dict["request_date"] = request_date
        if request_date_ms is not UNSET:
            field_dict["request_date_ms"] = request_date_ms
        if subscriber is not UNSET:
            field_dict["subscriber"] = subscriber

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscriber_subscriber import SubscriberSubscriber

        d = src_dict.copy()
        request_date = d.pop("request_date", UNSET)

        request_date_ms = d.pop("request_date_ms", UNSET)

        _subscriber = d.pop("subscriber", UNSET)
        subscriber: Union[Unset, SubscriberSubscriber]
        if isinstance(_subscriber, Unset):
            subscriber = UNSET
        else:
            subscriber = SubscriberSubscriber.from_dict(_subscriber)

        subscriber = cls(
            request_date=request_date,
            request_date_ms=request_date_ms,
            subscriber=subscriber,
        )

        subscriber.additional_properties = d
        return subscriber

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
