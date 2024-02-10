from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeferAGoogleSubscriptionBody")


@_attrs_define
class DeferAGoogleSubscriptionBody:
    """
    Attributes:
        expiry_time_ms (int): The desired next expiry time to assign to the subscription, in milliseconds since the
            Epoch. The given time must be later/greater than the current expiry time for the subscription.
    """

    expiry_time_ms: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expiry_time_ms = self.expiry_time_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiry_time_ms": expiry_time_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expiry_time_ms = d.pop("expiry_time_ms")

        defer_a_google_subscription_body = cls(
            expiry_time_ms=expiry_time_ms,
        )

        defer_a_google_subscription_body.additional_properties = d
        return defer_a_google_subscription_body

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
