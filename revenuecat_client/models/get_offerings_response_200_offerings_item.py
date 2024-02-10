from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_offerings_response_200_offerings_item_packages_item import (
        GetOfferingsResponse200OfferingsItemPackagesItem,
    )


T = TypeVar("T", bound="GetOfferingsResponse200OfferingsItem")


@_attrs_define
class GetOfferingsResponse200OfferingsItem:
    """
    Attributes:
        description (Union[Unset, str]):  Example: The default offering.
        identifier (Union[Unset, str]):  Example: default.
        packages (Union[Unset, List['GetOfferingsResponse200OfferingsItemPackagesItem']]):
    """

    description: Union[Unset, str] = UNSET
    identifier: Union[Unset, str] = UNSET
    packages: Union[
        Unset, List["GetOfferingsResponse200OfferingsItemPackagesItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        identifier = self.identifier

        packages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_offerings_response_200_offerings_item_packages_item import (
            GetOfferingsResponse200OfferingsItemPackagesItem,
        )

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        packages = []
        _packages = d.pop("packages", UNSET)
        for packages_item_data in _packages or []:
            packages_item = GetOfferingsResponse200OfferingsItemPackagesItem.from_dict(
                packages_item_data
            )

            packages.append(packages_item)

        get_offerings_response_200_offerings_item = cls(
            description=description,
            identifier=identifier,
            packages=packages,
        )

        get_offerings_response_200_offerings_item.additional_properties = d
        return get_offerings_response_200_offerings_item

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
