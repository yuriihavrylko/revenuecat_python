from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.customer_attribute_reserved_name import CustomerAttributeReservedName

T = TypeVar("T", bound="SetCustomerAttributesBodyAttributesItem")


@_attrs_define
class SetCustomerAttributesBodyAttributesItem:
    """
    Example:
        cat@revenuecat.com

    Attributes:
        name (Union[CustomerAttributeReservedName, str]): The name of the attribute Example: $email.
        value (Union[None, str]): The value of the attribute. Use null to delete the attribute.
    """

    name: Union[CustomerAttributeReservedName, str]
    value: Union[None, str]

    def to_dict(self) -> Dict[str, Any]:
        name: str
        if isinstance(self.name, CustomerAttributeReservedName):
            name = self.name.value
        else:
            name = self.name

        value: Union[None, str]
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[CustomerAttributeReservedName, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_0 = CustomerAttributeReservedName(data)

                return name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[CustomerAttributeReservedName, str], data)

        name = _parse_name(d.pop("name"))

        def _parse_value(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        value = _parse_value(d.pop("value"))

        set_customer_attributes_body_attributes_item = cls(
            name=name,
            value=value,
        )

        return set_customer_attributes_body_attributes_item
