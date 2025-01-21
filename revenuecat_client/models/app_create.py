from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_create_type import AppCreateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_app_create_amazon import AmazonAppCreateAmazon
    from ..models.app_store_app_create_app_store import AppStoreAppCreateAppStore
    from ..models.mac_app_store_app_create_mac_app_store import (
        MacAppStoreAppCreateMacAppStore,
    )
    from ..models.play_store_app_create_play_store import PlayStoreAppCreatePlayStore
    from ..models.rc_billing_app_create_rc_billing_type_0 import (
        RCBillingAppCreateRcBillingType0,
    )
    from ..models.roku_app_create_roku_type_0 import RokuAppCreateRokuType0
    from ..models.stripe_app_create_stripe import StripeAppCreateStripe


T = TypeVar("T", bound="AppCreate")


@_attrs_define
class AppCreate:
    """
    Attributes:
        name (str): The name of the app
        type (AppCreateType): The platform of the app.
            Mac App Store is disabled by default. See [Legacy Mac Apps](https://www.revenuecat.com/docs/legacy-mac-apps) for
            more details.
        amazon (Union[Unset, AmazonAppCreateAmazon]): Amazon type details. Should only be used when type is amazon.
        app_store (Union[Unset, AppStoreAppCreateAppStore]): App Store type details. Should only be used when type is
            app_store.
        mac_app_store (Union[Unset, MacAppStoreAppCreateMacAppStore]): Mac App Store type details. Should only be used
            when type is mac_app_store.
        play_store (Union[Unset, PlayStoreAppCreatePlayStore]): Play Store type details. Should only be used when type
            is play_store.
        stripe (Union[Unset, StripeAppCreateStripe]): Stripe type details. Should only be used when type is stripe.
        rc_billing (Union['RCBillingAppCreateRcBillingType0', None, Unset]): Revenue Cat Billing Store type details
        roku (Union['RokuAppCreateRokuType0', None, Unset]): Roku Channel Store details. Should only be used when type
            is roku.
    """

    name: str
    type: AppCreateType
    amazon: Union[Unset, "AmazonAppCreateAmazon"] = UNSET
    app_store: Union[Unset, "AppStoreAppCreateAppStore"] = UNSET
    mac_app_store: Union[Unset, "MacAppStoreAppCreateMacAppStore"] = UNSET
    play_store: Union[Unset, "PlayStoreAppCreatePlayStore"] = UNSET
    stripe: Union[Unset, "StripeAppCreateStripe"] = UNSET
    rc_billing: Union["RCBillingAppCreateRcBillingType0", None, Unset] = UNSET
    roku: Union["RokuAppCreateRokuType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.rc_billing_app_create_rc_billing_type_0 import (
            RCBillingAppCreateRcBillingType0,
        )
        from ..models.roku_app_create_roku_type_0 import RokuAppCreateRokuType0

        name = self.name

        type = self.type.value

        amazon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amazon, Unset):
            amazon = self.amazon.to_dict()

        app_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.app_store, Unset):
            app_store = self.app_store.to_dict()

        mac_app_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mac_app_store, Unset):
            mac_app_store = self.mac_app_store.to_dict()

        play_store: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.play_store, Unset):
            play_store = self.play_store.to_dict()

        stripe: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stripe, Unset):
            stripe = self.stripe.to_dict()

        rc_billing: Union[Dict[str, Any], None, Unset]
        if isinstance(self.rc_billing, Unset):
            rc_billing = UNSET
        elif isinstance(self.rc_billing, RCBillingAppCreateRcBillingType0):
            rc_billing = self.rc_billing.to_dict()
        else:
            rc_billing = self.rc_billing

        roku: Union[Dict[str, Any], None, Unset]
        if isinstance(self.roku, Unset):
            roku = UNSET
        elif isinstance(self.roku, RokuAppCreateRokuType0):
            roku = self.roku.to_dict()
        else:
            roku = self.roku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if amazon is not UNSET:
            field_dict["amazon"] = amazon
        if app_store is not UNSET:
            field_dict["app_store"] = app_store
        if mac_app_store is not UNSET:
            field_dict["mac_app_store"] = mac_app_store
        if play_store is not UNSET:
            field_dict["play_store"] = play_store
        if stripe is not UNSET:
            field_dict["stripe"] = stripe
        if rc_billing is not UNSET:
            field_dict["rc_billing"] = rc_billing
        if roku is not UNSET:
            field_dict["roku"] = roku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_app_create_amazon import AmazonAppCreateAmazon
        from ..models.app_store_app_create_app_store import AppStoreAppCreateAppStore
        from ..models.mac_app_store_app_create_mac_app_store import (
            MacAppStoreAppCreateMacAppStore,
        )
        from ..models.play_store_app_create_play_store import (
            PlayStoreAppCreatePlayStore,
        )
        from ..models.rc_billing_app_create_rc_billing_type_0 import (
            RCBillingAppCreateRcBillingType0,
        )
        from ..models.roku_app_create_roku_type_0 import RokuAppCreateRokuType0
        from ..models.stripe_app_create_stripe import StripeAppCreateStripe

        d = src_dict.copy()
        name = d.pop("name")

        type = AppCreateType(d.pop("type"))

        _amazon = d.pop("amazon", UNSET)
        amazon: Union[Unset, AmazonAppCreateAmazon]
        if isinstance(_amazon, Unset):
            amazon = UNSET
        else:
            amazon = AmazonAppCreateAmazon.from_dict(_amazon)

        _app_store = d.pop("app_store", UNSET)
        app_store: Union[Unset, AppStoreAppCreateAppStore]
        if isinstance(_app_store, Unset):
            app_store = UNSET
        else:
            app_store = AppStoreAppCreateAppStore.from_dict(_app_store)

        _mac_app_store = d.pop("mac_app_store", UNSET)
        mac_app_store: Union[Unset, MacAppStoreAppCreateMacAppStore]
        if isinstance(_mac_app_store, Unset):
            mac_app_store = UNSET
        else:
            mac_app_store = MacAppStoreAppCreateMacAppStore.from_dict(_mac_app_store)

        _play_store = d.pop("play_store", UNSET)
        play_store: Union[Unset, PlayStoreAppCreatePlayStore]
        if isinstance(_play_store, Unset):
            play_store = UNSET
        else:
            play_store = PlayStoreAppCreatePlayStore.from_dict(_play_store)

        _stripe = d.pop("stripe", UNSET)
        stripe: Union[Unset, StripeAppCreateStripe]
        if isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = StripeAppCreateStripe.from_dict(_stripe)

        def _parse_rc_billing(
            data: object,
        ) -> Union["RCBillingAppCreateRcBillingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rc_billing_type_0 = RCBillingAppCreateRcBillingType0.from_dict(data)

                return rc_billing_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RCBillingAppCreateRcBillingType0", None, Unset], data)

        rc_billing = _parse_rc_billing(d.pop("rc_billing", UNSET))

        def _parse_roku(data: object) -> Union["RokuAppCreateRokuType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                roku_type_0 = RokuAppCreateRokuType0.from_dict(data)

                return roku_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RokuAppCreateRokuType0", None, Unset], data)

        roku = _parse_roku(d.pop("roku", UNSET))

        app_create = cls(
            name=name,
            type=type,
            amazon=amazon,
            app_store=app_store,
            mac_app_store=mac_app_store,
            play_store=play_store,
            stripe=stripe,
            rc_billing=rc_billing,
            roku=roku,
        )

        app_create.additional_properties = d
        return app_create

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
