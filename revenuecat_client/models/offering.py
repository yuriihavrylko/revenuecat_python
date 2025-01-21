from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offering_object import OfferingObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offering_package_list import OfferingPackageList


T = TypeVar("T", bound="Offering")


@_attrs_define
class Offering:
    """
    Attributes:
        object_ (OfferingObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the offering Example: ofrnge1a2b3c4d5.
        lookup_key (str): A custom identifier of the entitlement Example: default.
        display_name (str): The display name of the offering Example: The standard set of packages.
        is_current (bool): Indicates if the offering is the current offering Example: True.
        created_at (int): The date the offering was created at in ms since epoch Example: 1658399423658.
        project_id (str): ID of the project to which the offering belongs Example: proj1ab2c3d4.
        metadata (Union[Unset, Any]): Custom metadata of the offering
        packages (Union['OfferingPackageList', None, Unset]):
    """

    object_: OfferingObject
    id: str
    lookup_key: str
    display_name: str
    is_current: bool
    created_at: int
    project_id: str
    metadata: Union[Unset, Any] = UNSET
    packages: Union["OfferingPackageList", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.offering_package_list import OfferingPackageList

        object_ = self.object_.value

        id = self.id

        lookup_key = self.lookup_key

        display_name = self.display_name

        is_current = self.is_current

        created_at = self.created_at

        project_id = self.project_id

        metadata = self.metadata

        packages: Union[Dict[str, Any], None, Unset]
        if isinstance(self.packages, Unset):
            packages = UNSET
        elif isinstance(self.packages, OfferingPackageList):
            packages = self.packages.to_dict()
        else:
            packages = self.packages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "lookup_key": lookup_key,
                "display_name": display_name,
                "is_current": is_current,
                "created_at": created_at,
                "project_id": project_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.offering_package_list import OfferingPackageList

        d = src_dict.copy()
        object_ = OfferingObject(d.pop("object"))

        id = d.pop("id")

        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        is_current = d.pop("is_current")

        created_at = d.pop("created_at")

        project_id = d.pop("project_id")

        metadata = d.pop("metadata", UNSET)

        def _parse_packages(data: object) -> Union["OfferingPackageList", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                packages_type_0 = OfferingPackageList.from_dict(data)

                return packages_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OfferingPackageList", None, Unset], data)

        packages = _parse_packages(d.pop("packages", UNSET))

        offering = cls(
            object_=object_,
            id=id,
            lookup_key=lookup_key,
            display_name=display_name,
            is_current=is_current,
            created_at=created_at,
            project_id=project_id,
            metadata=metadata,
            packages=packages,
        )

        offering.additional_properties = d
        return offering

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
