from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_attribute_object import CustomerAttributeObject

T = TypeVar("T", bound="CustomerAttribute")


@_attrs_define
class CustomerAttribute:
    """
    Attributes:
        object_ (CustomerAttributeObject): String representing the object's type. Objects of the same type share the
            same value.
        name (str): The name of the attribute. Reserved attributes are prefixed with a `$`. Example: $email.
        value (Union[None, str]): The value of the attribute. Example: garfield@revenuecat.com.
        updated_at (int): The time when the attribute was last updated. Example: 1658399423658.
    """

    object_: CustomerAttributeObject
    name: str
    value: Union[None, str]
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        name = self.name

        value: Union[None, str]
        value = self.value

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "name": name,
                "value": value,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = CustomerAttributeObject(d.pop("object"))

        name = d.pop("name")

        def _parse_value(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        value = _parse_value(d.pop("value"))

        updated_at = d.pop("updated_at")

        customer_attribute = cls(
            object_=object_,
            name=name,
            value=value,
            updated_at=updated_at,
        )

        customer_attribute.additional_properties = d
        return customer_attribute

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
