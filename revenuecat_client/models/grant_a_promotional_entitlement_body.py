import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantAPromotionalEntitlementBody")


@_attrs_define
class GrantAPromotionalEntitlementBody:
    """
    Attributes:
        duration (str): How long of a duration to grant the promotional entitlement for. See below for possible values.
        start_time_ms (Union[Unset, datetime.datetime]): A Unix epoch in milliseconds for when the promotional
            entitlement should have been considered as started. If not provided, the entitlement will be granted
            immediately. Future dates will also be granted immediately and will be active until the expiration date lapses.
    """

    duration: str
    start_time_ms: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration = self.duration

        start_time_ms: Union[Unset, str] = UNSET
        if not isinstance(self.start_time_ms, Unset):
            start_time_ms = self.start_time_ms.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
            }
        )
        if start_time_ms is not UNSET:
            field_dict["start_time_ms"] = start_time_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duration = d.pop("duration")

        _start_time_ms = d.pop("start_time_ms", UNSET)
        start_time_ms: Union[Unset, datetime.datetime]
        if isinstance(_start_time_ms, Unset):
            start_time_ms = UNSET
        else:
            start_time_ms = isoparse(_start_time_ms)

        grant_a_promotional_entitlement_body = cls(
            duration=duration,
            start_time_ms=start_time_ms,
        )

        grant_a_promotional_entitlement_body.additional_properties = d
        return grant_a_promotional_entitlement_body

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
