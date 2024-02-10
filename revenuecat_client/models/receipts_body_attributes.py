from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.receipts_body_attributes_key_name import ReceiptsBodyAttributesKeyName


T = TypeVar("T", bound="ReceiptsBodyAttributes")


@_attrs_define
class ReceiptsBodyAttributes:
    """
    Attributes:
        key_name (Union[Unset, ReceiptsBodyAttributesKeyName]): Mapping of key names to subscriber attribute objects.
            See the [attributes object](ref:subscribers#the-subscriber-attribute-object).
    """

    key_name: Union[Unset, "ReceiptsBodyAttributesKeyName"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_name, Unset):
            key_name = self.key_name.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_name is not UNSET:
            field_dict["key_name"] = key_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.receipts_body_attributes_key_name import (
            ReceiptsBodyAttributesKeyName,
        )

        d = src_dict.copy()
        _key_name = d.pop("key_name", UNSET)
        key_name: Union[Unset, ReceiptsBodyAttributesKeyName]
        if isinstance(_key_name, Unset):
            key_name = UNSET
        else:
            key_name = ReceiptsBodyAttributesKeyName.from_dict(_key_name)

        receipts_body_attributes = cls(
            key_name=key_name,
        )

        receipts_body_attributes.additional_properties = d
        return receipts_body_attributes

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
