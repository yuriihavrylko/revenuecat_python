from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_object import ProjectObject

T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """
    Attributes:
        object_ (ProjectObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the project Example: proj1ab2c3d4.
        name (str): The name of the project Example: MagicWeather.
        created_at (int): The date when the project was created in ms since epoch Example: 1658399423658.
    """

    object_: ProjectObject
    id: str
    name: str
    created_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        created_at = self.created_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = ProjectObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        project = cls(
            object_=object_,
            id=id,
            name=name,
            created_at=created_at,
        )

        project.additional_properties = d
        return project

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
