from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_subscriptions_annual import (
        SubscriberSubscriberSubscriptionsAnnual,
    )
    from ..models.subscriber_subscriber_subscriptions_onemonth import (
        SubscriberSubscriberSubscriptionsOnemonth,
    )
    from ..models.subscriber_subscriber_subscriptions_rc_promo_pro_cat_monthly import (
        SubscriberSubscriberSubscriptionsRcPromoProCatMonthly,
    )


T = TypeVar("T", bound="SubscriberSubscriberSubscriptions")


@_attrs_define
class SubscriberSubscriberSubscriptions:
    """
    Attributes:
        annual (Union[Unset, SubscriberSubscriberSubscriptionsAnnual]):
        onemonth (Union[Unset, SubscriberSubscriberSubscriptionsOnemonth]):
        rc_promo_pro_cat_monthly (Union[Unset, SubscriberSubscriberSubscriptionsRcPromoProCatMonthly]):
    """

    annual: Union[Unset, "SubscriberSubscriberSubscriptionsAnnual"] = UNSET
    onemonth: Union[Unset, "SubscriberSubscriberSubscriptionsOnemonth"] = UNSET
    rc_promo_pro_cat_monthly: Union[
        Unset, "SubscriberSubscriberSubscriptionsRcPromoProCatMonthly"
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annual: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annual, Unset):
            annual = self.annual.to_dict()

        onemonth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.onemonth, Unset):
            onemonth = self.onemonth.to_dict()

        rc_promo_pro_cat_monthly: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rc_promo_pro_cat_monthly, Unset):
            rc_promo_pro_cat_monthly = self.rc_promo_pro_cat_monthly.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annual is not UNSET:
            field_dict["annual"] = annual
        if onemonth is not UNSET:
            field_dict["onemonth"] = onemonth
        if rc_promo_pro_cat_monthly is not UNSET:
            field_dict["rc_promo_pro_cat_monthly"] = rc_promo_pro_cat_monthly

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscriber_subscriber_subscriptions_annual import (
            SubscriberSubscriberSubscriptionsAnnual,
        )
        from ..models.subscriber_subscriber_subscriptions_onemonth import (
            SubscriberSubscriberSubscriptionsOnemonth,
        )
        from ..models.subscriber_subscriber_subscriptions_rc_promo_pro_cat_monthly import (
            SubscriberSubscriberSubscriptionsRcPromoProCatMonthly,
        )

        d = src_dict.copy()
        _annual = d.pop("annual", UNSET)
        annual: Union[Unset, SubscriberSubscriberSubscriptionsAnnual]
        if isinstance(_annual, Unset):
            annual = UNSET
        else:
            annual = SubscriberSubscriberSubscriptionsAnnual.from_dict(_annual)

        _onemonth = d.pop("onemonth", UNSET)
        onemonth: Union[Unset, SubscriberSubscriberSubscriptionsOnemonth]
        if isinstance(_onemonth, Unset):
            onemonth = UNSET
        else:
            onemonth = SubscriberSubscriberSubscriptionsOnemonth.from_dict(_onemonth)

        _rc_promo_pro_cat_monthly = d.pop("rc_promo_pro_cat_monthly", UNSET)
        rc_promo_pro_cat_monthly: Union[
            Unset, SubscriberSubscriberSubscriptionsRcPromoProCatMonthly
        ]
        if isinstance(_rc_promo_pro_cat_monthly, Unset):
            rc_promo_pro_cat_monthly = UNSET
        else:
            rc_promo_pro_cat_monthly = (
                SubscriberSubscriberSubscriptionsRcPromoProCatMonthly.from_dict(
                    _rc_promo_pro_cat_monthly
                )
            )

        subscriber_subscriber_subscriptions = cls(
            annual=annual,
            onemonth=onemonth,
            rc_promo_pro_cat_monthly=rc_promo_pro_cat_monthly,
        )

        subscriber_subscriber_subscriptions.additional_properties = d
        return subscriber_subscriber_subscriptions

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
