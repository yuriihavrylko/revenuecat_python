from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deleted_object_object import DeletedObjectObject

T = TypeVar("T", bound="DeletedObject")


@_attrs_define
class DeletedObject:
    """
    Attributes:
        object_ (DeletedObjectObject): The type of the deleted object
        id (str): The ID of the deleted object
        deleted_at (int): The date when the object was deleted in ms since epoch Example: 1658399423658.
    """

    object_: DeletedObjectObject
    id: str
    deleted_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        deleted_at = self.deleted_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "deleted_at": deleted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = DeletedObjectObject(d.pop("object"))

        id = d.pop("id")

        deleted_at = d.pop("deleted_at")

        deleted_object = cls(
            object_=object_,
            id=id,
            deleted_at=deleted_at,
        )

        deleted_object.additional_properties = d
        return deleted_object

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
