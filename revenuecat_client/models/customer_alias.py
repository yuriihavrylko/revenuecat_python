from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_alias_object import CustomerAliasObject

T = TypeVar("T", bound="CustomerAlias")


@_attrs_define
class CustomerAlias:
    """
    Attributes:
        object_ (CustomerAliasObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        created_at (int): The time when the alias was created Example: 1658399423658.
    """

    object_: CustomerAliasObject
    id: str
    created_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = CustomerAliasObject(d.pop("object"))

        id = d.pop("id")

        created_at = d.pop("created_at")

        customer_alias = cls(
            object_=object_,
            id=id,
            created_at=created_at,
        )

        customer_alias.additional_properties = d
        return customer_alias

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
