import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReceiptsBodyAttributesKeyName")


@_attrs_define
class ReceiptsBodyAttributesKeyName:
    """Mapping of key names to subscriber attribute objects. See the [attributes object](ref:subscribers#the-subscriber-
    attribute-object).

        Attributes:
            value (str): The value of the attribute. If the value is `null` or an empty string, the attribute will be
                deleted.
            updated_at_ms (Union[Unset, datetime.datetime]): UNIX epoch in milliseconds of when the attribute was updated.
                This value is used to resolve conflicts, an attribute will only be updated if the new `updated_at_ms` value is
                newer than the value for the stored attribute.
    """

    value: str
    updated_at_ms: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        value = self.value

        updated_at_ms: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at_ms, Unset):
            updated_at_ms = self.updated_at_ms.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if updated_at_ms is not UNSET:
            field_dict["updated_at_ms"] = updated_at_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        value = d.pop("value")

        _updated_at_ms = d.pop("updated_at_ms", UNSET)
        updated_at_ms: Union[Unset, datetime.datetime]
        if isinstance(_updated_at_ms, Unset):
            updated_at_ms = UNSET
        else:
            updated_at_ms = isoparse(_updated_at_ms)

        receipts_body_attributes_key_name = cls(
            value=value,
            updated_at_ms=updated_at_ms,
        )

        receipts_body_attributes_key_name.additional_properties = d
        return receipts_body_attributes_key_name

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
