from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_customer_body_attributes_item import (
        CreateCustomerBodyAttributesItem,
    )


T = TypeVar("T", bound="CreateCustomerBody")


@_attrs_define
class CreateCustomerBody:
    """
    Attributes:
        id (str): The ID of the customer Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        attributes (Union[Unset, List['CreateCustomerBodyAttributesItem']]):
    """

    id: str
    attributes: Union[Unset, List["CreateCustomerBodyAttributesItem"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_customer_body_attributes_item import (
            CreateCustomerBodyAttributesItem,
        )

        d = src_dict.copy()
        id = d.pop("id")

        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = CreateCustomerBodyAttributesItem.from_dict(
                attributes_item_data
            )

            attributes.append(attributes_item)

        create_customer_body = cls(
            id=id,
            attributes=attributes,
        )

        return create_customer_body
