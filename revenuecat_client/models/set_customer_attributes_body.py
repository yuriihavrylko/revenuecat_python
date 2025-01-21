from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.set_customer_attributes_body_attributes_item import (
        SetCustomerAttributesBodyAttributesItem,
    )


T = TypeVar("T", bound="SetCustomerAttributesBody")


@_attrs_define
class SetCustomerAttributesBody:
    """
    Attributes:
        attributes (List['SetCustomerAttributesBodyAttributesItem']):
    """

    attributes: List["SetCustomerAttributesBodyAttributesItem"]

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()
            attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.set_customer_attributes_body_attributes_item import (
            SetCustomerAttributesBodyAttributesItem,
        )

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = SetCustomerAttributesBodyAttributesItem.from_dict(
                attributes_item_data
            )

            attributes.append(attributes_item)

        set_customer_attributes_body = cls(
            attributes=attributes,
        )

        return set_customer_attributes_body
