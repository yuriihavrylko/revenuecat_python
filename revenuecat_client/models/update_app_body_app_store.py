from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppBodyAppStore")


@_attrs_define
class UpdateAppBodyAppStore:
    """App Store type details. Should only be used when type is app_store.

    Attributes:
        bundle_id (Union[Unset, str]): The bundle ID of the app
        shared_secret (Union[None, Unset, str]): The shared secret of the app
    """

    bundle_id: Union[Unset, str] = UNSET
    shared_secret: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bundle_id = self.bundle_id

        shared_secret: Union[None, Unset, str]
        if isinstance(self.shared_secret, Unset):
            shared_secret = UNSET
        else:
            shared_secret = self.shared_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundle_id is not UNSET:
            field_dict["bundle_id"] = bundle_id
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bundle_id = d.pop("bundle_id", UNSET)

        def _parse_shared_secret(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shared_secret = _parse_shared_secret(d.pop("shared_secret", UNSET))

        update_app_body_app_store = cls(
            bundle_id=bundle_id,
            shared_secret=shared_secret,
        )

        update_app_body_app_store.additional_properties = d
        return update_app_body_app_store

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
