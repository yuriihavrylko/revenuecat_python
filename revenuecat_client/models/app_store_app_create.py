from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_store_app_create_app_store import AppStoreAppCreateAppStore


T = TypeVar("T", bound="AppStoreAppCreate")


@_attrs_define
class AppStoreAppCreate:
    """
    Attributes:
        app_store (Union[Unset, AppStoreAppCreateAppStore]): App Store type details. Should only be used when type is
            app_store.
    """

    app_store: Union[Unset, "AppStoreAppCreateAppStore"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app_store, Unset):
            app_store = self.app_store.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if app_store is not UNSET:
            field_dict["app_store"] = app_store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_store_app_create_app_store import AppStoreAppCreateAppStore

        d = src_dict.copy()
        _app_store = d.pop("app_store", UNSET)
        app_store: Union[Unset, AppStoreAppCreateAppStore]
        if isinstance(_app_store, Unset):
            app_store = UNSET
        else:
            app_store = AppStoreAppCreateAppStore.from_dict(_app_store)

        app_store_app_create = cls(
            app_store=app_store,
        )

        app_store_app_create.additional_properties = d
        return app_store_app_create

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
