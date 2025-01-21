from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.app_object import AppObject
from ..models.app_type import AppType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_app_amazon import AmazonAppAmazon
    from ..models.app_store_app_app_store import AppStoreAppAppStore
    from ..models.mac_app_store_app_mac_app_store import MacAppStoreAppMacAppStore
    from ..models.play_store_app_play_store import PlayStoreAppPlayStore
    from ..models.rc_billing_app_rc_billing import RCBillingAppRcBilling
    from ..models.roku_app_roku import RokuAppRoku
    from ..models.stripe_app_stripe import StripeAppStripe


T = TypeVar("T", bound="App")


@_attrs_define
class App:
    """
    Attributes:
        object_ (AppObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the app Example: app1a2b3c4.
        name (str): The name of the app
        created_at (int): The date when the app was created in ms since epoch Example: 1658399423658.
        type (AppType): The platform of the app Example: app_store.
        project_id (str): The id of the project Example: proj1a2b3c4.
        amazon (Union[Unset, AmazonAppAmazon]): Amazon type details
        app_store (Union[Unset, AppStoreAppAppStore]): App Store type details
        mac_app_store (Union[Unset, MacAppStoreAppMacAppStore]): Legacy Mac App Store type details
        play_store (Union[Unset, PlayStoreAppPlayStore]): Play Store type details
        stripe (Union[Unset, StripeAppStripe]): Stripe type details
        rc_billing (Union[Unset, RCBillingAppRcBilling]): Revenue Cat Billing Store type details
        roku (Union[Unset, RokuAppRoku]): Roku Channel Store type details
    """

    object_: AppObject
    id: str
    name: str
    created_at: int
    type: AppType
    project_id: str
    amazon: Union[Unset, "AmazonAppAmazon"] = UNSET
    app_store: Union[Unset, "AppStoreAppAppStore"] = UNSET
    mac_app_store: Union[Unset, "MacAppStoreAppMacAppStore"] = UNSET
    play_store: Union[Unset, "PlayStoreAppPlayStore"] = UNSET
    stripe: Union[Unset, "StripeAppStripe"] = UNSET
    rc_billing: Union[Unset, "RCBillingAppRcBilling"] = UNSET
    roku: Union[Unset, "RokuAppRoku"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        created_at = self.created_at

        type = self.type.value

        project_id = self.project_id

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
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "created_at": created_at,
                "type": type,
                "project_id": project_id,
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
        from ..models.amazon_app_amazon import AmazonAppAmazon
        from ..models.app_store_app_app_store import AppStoreAppAppStore
        from ..models.mac_app_store_app_mac_app_store import MacAppStoreAppMacAppStore
        from ..models.play_store_app_play_store import PlayStoreAppPlayStore
        from ..models.rc_billing_app_rc_billing import RCBillingAppRcBilling
        from ..models.roku_app_roku import RokuAppRoku
        from ..models.stripe_app_stripe import StripeAppStripe

        d = src_dict.copy()
        object_ = AppObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        type = AppType(d.pop("type"))

        project_id = d.pop("project_id")

        _amazon = d.pop("amazon", UNSET)
        amazon: Union[Unset, AmazonAppAmazon]
        if isinstance(_amazon, Unset):
            amazon = UNSET
        else:
            amazon = AmazonAppAmazon.from_dict(_amazon)

        _app_store = d.pop("app_store", UNSET)
        app_store: Union[Unset, AppStoreAppAppStore]
        if isinstance(_app_store, Unset):
            app_store = UNSET
        else:
            app_store = AppStoreAppAppStore.from_dict(_app_store)

        _mac_app_store = d.pop("mac_app_store", UNSET)
        mac_app_store: Union[Unset, MacAppStoreAppMacAppStore]
        if isinstance(_mac_app_store, Unset):
            mac_app_store = UNSET
        else:
            mac_app_store = MacAppStoreAppMacAppStore.from_dict(_mac_app_store)

        _play_store = d.pop("play_store", UNSET)
        play_store: Union[Unset, PlayStoreAppPlayStore]
        if isinstance(_play_store, Unset):
            play_store = UNSET
        else:
            play_store = PlayStoreAppPlayStore.from_dict(_play_store)

        _stripe = d.pop("stripe", UNSET)
        stripe: Union[Unset, StripeAppStripe]
        if isinstance(_stripe, Unset):
            stripe = UNSET
        else:
            stripe = StripeAppStripe.from_dict(_stripe)

        _rc_billing = d.pop("rc_billing", UNSET)
        rc_billing: Union[Unset, RCBillingAppRcBilling]
        if isinstance(_rc_billing, Unset):
            rc_billing = UNSET
        else:
            rc_billing = RCBillingAppRcBilling.from_dict(_rc_billing)

        _roku = d.pop("roku", UNSET)
        roku: Union[Unset, RokuAppRoku]
        if isinstance(_roku, Unset):
            roku = UNSET
        else:
            roku = RokuAppRoku.from_dict(_roku)

        app = cls(
            object_=object_,
            id=id,
            name=name,
            created_at=created_at,
            type=type,
            project_id=project_id,
            amazon=amazon,
            app_store=app_store,
            mac_app_store=mac_app_store,
            play_store=play_store,
            stripe=stripe,
            rc_billing=rc_billing,
            roku=roku,
        )

        app.additional_properties = d
        return app

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
