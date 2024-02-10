from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_subscriber_entitlements import (
        SubscriberSubscriberEntitlements,
    )
    from ..models.subscriber_subscriber_non_subscriptions import (
        SubscriberSubscriberNonSubscriptions,
    )
    from ..models.subscriber_subscriber_other_purchases import (
        SubscriberSubscriberOtherPurchases,
    )
    from ..models.subscriber_subscriber_subscriptions import (
        SubscriberSubscriberSubscriptions,
    )


T = TypeVar("T", bound="SubscriberSubscriber")


@_attrs_define
class SubscriberSubscriber:
    """
    Attributes:
        entitlements (Union[Unset, SubscriberSubscriberEntitlements]):
        first_seen (Union[Unset, str]):  Example: 2019-02-21T00:08:41Z.
        management_url (Union[Unset, str]):  Example: https://apps.apple.com/account/subscriptions.
        non_subscriptions (Union[Unset, SubscriberSubscriberNonSubscriptions]):
        original_app_user_id (Union[Unset, str]):  Example: XXX-XXXXX-XXXXX-XX.
        original_application_version (Union[Unset, str]):  Example: 1.0.
        original_purchase_date (Union[Unset, str]):  Example: 2019-01-30T23:54:10Z.
        other_purchases (Union[Unset, SubscriberSubscriberOtherPurchases]):
        subscriptions (Union[Unset, SubscriberSubscriberSubscriptions]):
    """

    entitlements: Union[Unset, "SubscriberSubscriberEntitlements"] = UNSET
    first_seen: Union[Unset, str] = UNSET
    management_url: Union[Unset, str] = UNSET
    non_subscriptions: Union[Unset, "SubscriberSubscriberNonSubscriptions"] = UNSET
    original_app_user_id: Union[Unset, str] = UNSET
    original_application_version: Union[Unset, str] = UNSET
    original_purchase_date: Union[Unset, str] = UNSET
    other_purchases: Union[Unset, "SubscriberSubscriberOtherPurchases"] = UNSET
    subscriptions: Union[Unset, "SubscriberSubscriberSubscriptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entitlements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = self.entitlements.to_dict()

        first_seen = self.first_seen

        management_url = self.management_url

        non_subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.non_subscriptions, Unset):
            non_subscriptions = self.non_subscriptions.to_dict()

        original_app_user_id = self.original_app_user_id

        original_application_version = self.original_application_version

        original_purchase_date = self.original_purchase_date

        other_purchases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.other_purchases, Unset):
            other_purchases = self.other_purchases.to_dict()

        subscriptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements
        if first_seen is not UNSET:
            field_dict["first_seen"] = first_seen
        if management_url is not UNSET:
            field_dict["management_url"] = management_url
        if non_subscriptions is not UNSET:
            field_dict["non_subscriptions"] = non_subscriptions
        if original_app_user_id is not UNSET:
            field_dict["original_app_user_id"] = original_app_user_id
        if original_application_version is not UNSET:
            field_dict["original_application_version"] = original_application_version
        if original_purchase_date is not UNSET:
            field_dict["original_purchase_date"] = original_purchase_date
        if other_purchases is not UNSET:
            field_dict["other_purchases"] = other_purchases
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscriber_subscriber_entitlements import (
            SubscriberSubscriberEntitlements,
        )
        from ..models.subscriber_subscriber_non_subscriptions import (
            SubscriberSubscriberNonSubscriptions,
        )
        from ..models.subscriber_subscriber_other_purchases import (
            SubscriberSubscriberOtherPurchases,
        )
        from ..models.subscriber_subscriber_subscriptions import (
            SubscriberSubscriberSubscriptions,
        )

        d = src_dict.copy()
        _entitlements = d.pop("entitlements", UNSET)
        entitlements: Union[Unset, SubscriberSubscriberEntitlements]
        if isinstance(_entitlements, Unset):
            entitlements = UNSET
        else:
            entitlements = SubscriberSubscriberEntitlements.from_dict(_entitlements)

        first_seen = d.pop("first_seen", UNSET)

        management_url = d.pop("management_url", UNSET)

        _non_subscriptions = d.pop("non_subscriptions", UNSET)
        non_subscriptions: Union[Unset, SubscriberSubscriberNonSubscriptions]
        if isinstance(_non_subscriptions, Unset):
            non_subscriptions = UNSET
        else:
            non_subscriptions = SubscriberSubscriberNonSubscriptions.from_dict(
                _non_subscriptions
            )

        original_app_user_id = d.pop("original_app_user_id", UNSET)

        original_application_version = d.pop("original_application_version", UNSET)

        original_purchase_date = d.pop("original_purchase_date", UNSET)

        _other_purchases = d.pop("other_purchases", UNSET)
        other_purchases: Union[Unset, SubscriberSubscriberOtherPurchases]
        if isinstance(_other_purchases, Unset):
            other_purchases = UNSET
        else:
            other_purchases = SubscriberSubscriberOtherPurchases.from_dict(
                _other_purchases
            )

        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: Union[Unset, SubscriberSubscriberSubscriptions]
        if isinstance(_subscriptions, Unset):
            subscriptions = UNSET
        else:
            subscriptions = SubscriberSubscriberSubscriptions.from_dict(_subscriptions)

        subscriber_subscriber = cls(
            entitlements=entitlements,
            first_seen=first_seen,
            management_url=management_url,
            non_subscriptions=non_subscriptions,
            original_app_user_id=original_app_user_id,
            original_application_version=original_application_version,
            original_purchase_date=original_purchase_date,
            other_purchases=other_purchases,
            subscriptions=subscriptions,
        )

        subscriber_subscriber.additional_properties = d
        return subscriber_subscriber

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
