from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscriber_attributes_body_attributes import (
        UpdateSubscriberAttributesBodyAttributes,
    )


T = TypeVar("T", bound="UpdateSubscriberAttributesBody")


@_attrs_define
class UpdateSubscriberAttributesBody:
    """
    Attributes:
        attributes (Union[Unset, UpdateSubscriberAttributesBodyAttributes]):
    """

    attributes: Union[Unset, "UpdateSubscriberAttributesBodyAttributes"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_subscriber_attributes_body_attributes import (
            UpdateSubscriberAttributesBodyAttributes,
        )

        d = src_dict.copy()
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, UpdateSubscriberAttributesBodyAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UpdateSubscriberAttributesBodyAttributes.from_dict(_attributes)

        update_subscriber_attributes_body = cls(
            attributes=attributes,
        )

        update_subscriber_attributes_body.additional_properties = d
        return update_subscriber_attributes_body

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
