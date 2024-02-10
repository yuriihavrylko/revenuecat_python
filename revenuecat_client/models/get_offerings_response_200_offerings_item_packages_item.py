from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOfferingsResponse200OfferingsItemPackagesItem")


@_attrs_define
class GetOfferingsResponse200OfferingsItemPackagesItem:
    """
    Attributes:
        identifier (Union[Unset, str]):  Example: $rc_monthly.
        platform_product_identifier (Union[Unset, str]):  Example: monthly_free_trial.
    """

    identifier: Union[Unset, str] = UNSET
    platform_product_identifier: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier

        platform_product_identifier = self.platform_product_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if platform_product_identifier is not UNSET:
            field_dict["platform_product_identifier"] = platform_product_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        platform_product_identifier = d.pop("platform_product_identifier", UNSET)

        get_offerings_response_200_offerings_item_packages_item = cls(
            identifier=identifier,
            platform_product_identifier=platform_product_identifier,
        )

        get_offerings_response_200_offerings_item_packages_item.additional_properties = d
        return get_offerings_response_200_offerings_item_packages_item

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
