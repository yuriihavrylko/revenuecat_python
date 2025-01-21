from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.customer_attribute_reserved_name import CustomerAttributeReservedName

T = TypeVar("T", bound="CreateCustomerBodyAttributesItem")


@_attrs_define
class CreateCustomerBodyAttributesItem:
    """
    Attributes:
        name (Union[CustomerAttributeReservedName, str]): The name of the attribute Example: $email.
        value (str): The value of the attribute Example: cat@revenuecat.com.
    """

    name: Union[CustomerAttributeReservedName, str]
    value: str

    def to_dict(self) -> Dict[str, Any]:
        name: str
        if isinstance(self.name, CustomerAttributeReservedName):
            name = self.name.value
        else:
            name = self.name

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

        value = d.pop("value")

        create_customer_body_attributes_item = cls(
            name=name,
            value=value,
        )

        return create_customer_body_attributes_item
