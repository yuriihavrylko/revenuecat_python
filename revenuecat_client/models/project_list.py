from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_list_object import ProjectListObject

if TYPE_CHECKING:
    from ..models.project import Project


T = TypeVar("T", bound="ProjectList")


@_attrs_define
class ProjectList:
    """
    Attributes:
        object_ (ProjectListObject): String representing the object's type. Objects of the same type share the same
            value. Always has the value `list`.
        items (List['Project']): Details about each object.
        next_page (Union[None, str]): URL to access the next page of the projects. If not present / null, there is no
            next page Example: /v2/projects?starting_after=projab21dac.
        url (str): The URL where this list can be accessed. Example: /v2/projects.
    """

    object_: ProjectListObject
    items: List["Project"]
    next_page: Union[None, str]
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_page: Union[None, str]
        next_page = self.next_page

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "items": items,
                "next_page": next_page,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project import Project

        d = src_dict.copy()
        object_ = ProjectListObject(d.pop("object"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Project.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_page(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_page = _parse_next_page(d.pop("next_page"))

        url = d.pop("url")

        project_list = cls(
            object_=object_,
            items=items,
            next_page=next_page,
            url=url,
        )

        project_list.additional_properties = d
        return project_list

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
