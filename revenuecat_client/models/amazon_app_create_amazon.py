from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AmazonAppCreateAmazon")


@_attrs_define
class AmazonAppCreateAmazon:
    """Amazon type details. Should only be used when type is amazon.

    Attributes:
        package_name (str): The package name of the app
        shared_secret (Union[Unset, str]): Your Amazon Developer Identity Shared Key
    """

    package_name: str
    shared_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package_name = self.package_name

        shared_secret = self.shared_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "package_name": package_name,
            }
        )
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        package_name = d.pop("package_name")

        shared_secret = d.pop("shared_secret", UNSET)

        amazon_app_create_amazon = cls(
            package_name=package_name,
            shared_secret=shared_secret,
        )

        amazon_app_create_amazon.additional_properties = d
        return amazon_app_create_amazon

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
