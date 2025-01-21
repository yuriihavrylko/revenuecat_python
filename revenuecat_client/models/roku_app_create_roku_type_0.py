from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RokuAppCreateRokuType0")


@_attrs_define
class RokuAppCreateRokuType0:
    """Roku Channel Store details. Should only be used when type is roku.

    Attributes:
        roku_api_key (Union[None, Unset, str]): Roku Pay API key provided on the Roku Pay Web Services page.
        roku_channel_id (Union[None, Unset, str]): Channel ID provided on the Roku Channel page.
        roku_channel_name (Union[None, Unset, str]): Channel name that is displayed on the Roku Channel page.
    """

    roku_api_key: Union[None, Unset, str] = UNSET
    roku_channel_id: Union[None, Unset, str] = UNSET
    roku_channel_name: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        roku_api_key: Union[None, Unset, str]
        if isinstance(self.roku_api_key, Unset):
            roku_api_key = UNSET
        else:
            roku_api_key = self.roku_api_key

        roku_channel_id: Union[None, Unset, str]
        if isinstance(self.roku_channel_id, Unset):
            roku_channel_id = UNSET
        else:
            roku_channel_id = self.roku_channel_id

        roku_channel_name: Union[None, Unset, str]
        if isinstance(self.roku_channel_name, Unset):
            roku_channel_name = UNSET
        else:
            roku_channel_name = self.roku_channel_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roku_api_key is not UNSET:
            field_dict["roku_api_key"] = roku_api_key
        if roku_channel_id is not UNSET:
            field_dict["roku_channel_id"] = roku_channel_id
        if roku_channel_name is not UNSET:
            field_dict["roku_channel_name"] = roku_channel_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_roku_api_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        roku_api_key = _parse_roku_api_key(d.pop("roku_api_key", UNSET))

        def _parse_roku_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        roku_channel_id = _parse_roku_channel_id(d.pop("roku_channel_id", UNSET))

        def _parse_roku_channel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        roku_channel_name = _parse_roku_channel_name(d.pop("roku_channel_name", UNSET))

        roku_app_create_roku_type_0 = cls(
            roku_api_key=roku_api_key,
            roku_channel_id=roku_channel_id,
            roku_channel_name=roku_channel_name,
        )

        roku_app_create_roku_type_0.additional_properties = d
        return roku_app_create_roku_type_0

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
