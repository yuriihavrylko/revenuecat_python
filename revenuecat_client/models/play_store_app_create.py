from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.play_store_app_create_play_store import PlayStoreAppCreatePlayStore


T = TypeVar("T", bound="PlayStoreAppCreate")


@_attrs_define
class PlayStoreAppCreate:
    """
    Attributes:
        play_store (Union[Unset, PlayStoreAppCreatePlayStore]): Play Store type details. Should only be used when type
            is play_store.
    """

    play_store: Union[Unset, "PlayStoreAppCreatePlayStore"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        play_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.play_store, Unset):
            play_store = self.play_store.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if play_store is not UNSET:
            field_dict["play_store"] = play_store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.play_store_app_create_play_store import (
            PlayStoreAppCreatePlayStore,
        )

        d = src_dict.copy()
        _play_store = d.pop("play_store", UNSET)
        play_store: Union[Unset, PlayStoreAppCreatePlayStore]
        if isinstance(_play_store, Unset):
            play_store = UNSET
        else:
            play_store = PlayStoreAppCreatePlayStore.from_dict(_play_store)

        play_store_app_create = cls(
            play_store=play_store,
        )

        play_store_app_create.additional_properties = d
        return play_store_app_create

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
