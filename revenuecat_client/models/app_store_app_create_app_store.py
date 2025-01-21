from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppStoreAppCreateAppStore")


@_attrs_define
class AppStoreAppCreateAppStore:
    """App Store type details. Should only be used when type is app_store.

    Attributes:
        bundle_id (str): The bundle ID of the app
        subscription_private_key (str): PKCS /#8 In App Key downloaded from App Store Connect in PEM format. Copy the
            contents
            of the file in this field. See instructions on how to get it in:
            https://www.revenuecat.com/docs/in-app-purchase-key-configuration
        subscription_key_id (str): In App Key id. The ID of the downloaded in app key. You can get it from App Store
            Connect
        subscription_key_issuer (str): The key Issuer id. See instructions on how to obtain this in:
            https://www.revenuecat.com/docs/in-app-purchase-key-configuration#3-providing-the-issuer-id-to-revenuecat
        shared_secret (Union[Unset, str]): The shared secret of the app
    """

    bundle_id: str
    subscription_private_key: str
    subscription_key_id: str
    subscription_key_issuer: str
    shared_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bundle_id = self.bundle_id

        subscription_private_key = self.subscription_private_key

        subscription_key_id = self.subscription_key_id

        subscription_key_issuer = self.subscription_key_issuer

        shared_secret = self.shared_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bundle_id": bundle_id,
                "subscription_private_key": subscription_private_key,
                "subscription_key_id": subscription_key_id,
                "subscription_key_issuer": subscription_key_issuer,
            }
        )
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bundle_id = d.pop("bundle_id")

        subscription_private_key = d.pop("subscription_private_key")

        subscription_key_id = d.pop("subscription_key_id")

        subscription_key_issuer = d.pop("subscription_key_issuer")

        shared_secret = d.pop("shared_secret", UNSET)

        app_store_app_create_app_store = cls(
            bundle_id=bundle_id,
            subscription_private_key=subscription_private_key,
            subscription_key_id=subscription_key_id,
            subscription_key_issuer=subscription_key_issuer,
            shared_secret=shared_secret,
        )

        app_store_app_create_app_store.additional_properties = d
        return app_store_app_create_app_store

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
