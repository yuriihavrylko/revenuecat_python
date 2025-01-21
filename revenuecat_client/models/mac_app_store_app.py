from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_app_store_app_mac_app_store import MacAppStoreAppMacAppStore


T = TypeVar("T", bound="MacAppStoreApp")


@_attrs_define
class MacAppStoreApp:
    """
    Attributes:
        mac_app_store (Union[Unset, MacAppStoreAppMacAppStore]): Legacy Mac App Store type details
    """

    mac_app_store: Union[Unset, "MacAppStoreAppMacAppStore"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mac_app_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mac_app_store, Unset):
            mac_app_store = self.mac_app_store.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac_app_store is not UNSET:
            field_dict["mac_app_store"] = mac_app_store

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.mac_app_store_app_mac_app_store import MacAppStoreAppMacAppStore

        d = src_dict.copy()
        _mac_app_store = d.pop("mac_app_store", UNSET)
        mac_app_store: Union[Unset, MacAppStoreAppMacAppStore]
        if isinstance(_mac_app_store, Unset):
            mac_app_store = UNSET
        else:
            mac_app_store = MacAppStoreAppMacAppStore.from_dict(_mac_app_store)

        mac_app_store_app = cls(
            mac_app_store=mac_app_store,
        )

        mac_app_store_app.additional_properties = d
        return mac_app_store_app

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
