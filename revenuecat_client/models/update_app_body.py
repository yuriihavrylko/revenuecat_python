from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_app_body_amazon import UpdateAppBodyAmazon
    from ..models.update_app_body_app_store import UpdateAppBodyAppStore
    from ..models.update_app_body_mac_app_store import UpdateAppBodyMacAppStore
    from ..models.update_app_body_play_store import UpdateAppBodyPlayStore
    from ..models.update_app_body_rc_billing import UpdateAppBodyRcBilling
    from ..models.update_app_body_roku import UpdateAppBodyRoku
    from ..models.update_app_body_stripe import UpdateAppBodyStripe


T = TypeVar("T", bound="UpdateAppBody")


@_attrs_define
class UpdateAppBody:
    """
    Attributes:
        name (Union[Unset, str]): The name of the app Example: My App.
        amazon (Union[Unset, UpdateAppBodyAmazon]): Amazon type details. Should only be used when type is amazon.
        app_store (Union[Unset, UpdateAppBodyAppStore]): App Store type details. Should only be used when type is
            app_store.
        mac_app_store (Union[Unset, UpdateAppBodyMacAppStore]): Legacy Mac App Store type details. Should only be used
            when type is mac_app_store.
        play_store (Union[Unset, UpdateAppBodyPlayStore]): Play Store type details. Should only be used when type is
            play_store.
        stripe (Union[Unset, UpdateAppBodyStripe]): Stripe type details. Should only be used when type is stripe.
        rc_billing (Union[Unset, UpdateAppBodyRcBilling]): RevenueCat Billing type details. Should only be used when
            type is rc_billing.
        roku (Union[Unset, UpdateAppBodyRoku]): Roku Channel Store type details. Should only be used when type is roku.
    """

    name: Union[Unset, str] = UNSET
    amazon: Union[Unset, "UpdateAppBodyAmazon"] = UNSET
    app_store: Union[Unset, "UpdateAppBodyAppStore"] = UNSET
    mac_app_store: Union[Unset, "UpdateAppBodyMacAppStore"] = UNSET
    play_store: Union[Unset, "UpdateAppBodyPlayStore"] = UNSET
    stripe: Union[Unset, "UpdateAppBodyStripe"] = UNSET
    rc_billing: Union[Unset, "UpdateAppBodyRcBilling"] = UNSET
    roku: Union[Unset, "UpdateAppBodyRoku"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

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

        rc_billing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rc_billing, Unset):
            rc_billing = self.rc_billing.to_dict()

        roku: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.roku, Unset):
            roku = self.roku.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.update_app_body_amazon import UpdateAppBodyAmazon
        from ..models.update_app_body_app_store import UpdateAppBodyAppStore
        from ..models.update_app_body_mac_app_store import UpdateAppBodyMacAppStore
        from ..models.update_app_body_play_store import UpdateAppBodyPlayStore
        from ..models.update_app_body_rc_billing import UpdateAppBodyRcBilling
        from ..models.update_app_body_roku import UpdateAppBodyRoku
        from ..models.update_app_body_stripe import UpdateAppBodyStripe

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _amazon = d.pop("amazon", UNSET)
        amazon: Union[Unset, UpdateAppBodyAmazon]
        if isinstance(_amazon, Unset):
            amazon = UNSET
        else:
            amazon = UpdateAppBodyAmazon.from_dict(_amazon)

        _app_store = d.pop("app_store", UNSET)
        app_store: Union[Unset, UpdateAppBodyAppStore]
        if isinstance(_app_store, Unset):
            app_store = UNSET
        else:
            app_store = UpdateAppBodyAppStore.from_dict(_app_store)

        _mac_app_store = d.pop("mac_app_store", UNSET)
        mac_app_store: Union[Unset, UpdateAppBodyMacAppStore]
        if isinstance(_mac_app_store, Unset):
            mac_app_store = UNSET
        else:
            mac_app_store = UpdateAppBodyMacAppStore.from_dict(_mac_app_store)

        _play_store = d.pop("play_store", UNSET)
        play_store: Union[Unset, UpdateAppBodyPlayStore]
        if isinstance(_play_store, Unset):
            play_store = UNSET
        else:
            play_store = UpdateAppBodyPlayStore.from_dict(_play_store)

        _stripe = d.pop("stripe", UNSET)
        stripe: Union[Unset, UpdateAppBodyStripe]
        if isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = UpdateAppBodyStripe.from_dict(_stripe)

        _rc_billing = d.pop("rc_billing", UNSET)
        rc_billing: Union[Unset, UpdateAppBodyRcBilling]
        if isinstance(_rc_billing, Unset):
            rc_billing = UNSET
        else:
            rc_billing = UpdateAppBodyRcBilling.from_dict(_rc_billing)

        _roku = d.pop("roku", UNSET)
        roku: Union[Unset, UpdateAppBodyRoku]
        if isinstance(_roku, Unset):
            roku = UNSET
        else:
            roku = UpdateAppBodyRoku.from_dict(_roku)

        update_app_body = cls(
            name=name,
            amazon=amazon,
            app_store=app_store,
            mac_app_store=mac_app_store,
            play_store=play_store,
            stripe=stripe,
            rc_billing=rc_billing,
            roku=roku,
        )

        return update_app_body
