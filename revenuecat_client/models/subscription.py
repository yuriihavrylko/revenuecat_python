from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment import Environment
from ..models.ownership import Ownership
from ..models.subscription_auto_renewal_status import SubscriptionAutoRenewalStatus
from ..models.subscription_object import SubscriptionObject
from ..models.subscription_status import SubscriptionStatus
from ..models.subscription_store import SubscriptionStore
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monetary_amount import MonetaryAmount
    from ..models.subscription_entitlement_list import SubscriptionEntitlementList
    from ..models.subscription_pending_changes_type_0 import (
        SubscriptionPendingChangesType0,
    )


T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """
    Attributes:
        object_ (SubscriptionObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str): The ID of the subscription (generated by RevenueCat) Example: sub1ab2c3d4e5.
        customer_id (str): The ID of the customer Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        original_customer_id (str): The ID of the original customer. Relevant for subscriptions that were transferred
            from one customer to another Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        product_id (Union[None, str]): The RevenueCat ID of the product that the customer is subscribed to. Exists for
            all store types except for promotional. Example: prod1a2b3c4d5e.
        starts_at (int): The date when the subscription originally started in ms since epoch Example: 1658399423658.
        current_period_starts_at (int): The date when the subscription billing period started in ms since epoch Example:
            1658399423658.
        current_period_ends_at (Union[None, int]): The date when the subscription billing period is expected to end in
            ms since epoch. Can be null if the subscription is paused until an indefinite date. Example: 1658399423658.
        gives_access (bool): Determines whether the customer should currently be provided access to the entitlements
            associated with the subscription Example: True.
        pending_payment (bool): Determines whether there is a pending payment associated with the subscription Example:
            True.
        auto_renewal_status (SubscriptionAutoRenewalStatus): The auto renewal status of a subscription.<br><br>Possible
            values:<br>• `will_renew`: the subscription is currently set to automatically renew<br>• `will_not_renew`: the
            subscription is currently set to expire at the end of the period<br>• `will_change_product`: the subscription is
            currently set to change product at the end of the period (which might start a new subscription)<br>•
            `will_pause`: the subscription is currently set to pause at the end of the current period<br>•
            `requires_price_increase_consent`: the subscription will expire at the end of the current period unless the
            customer consents to the price increase<br>• `has_already_renewed`: the customer has already been charged for
            the upcoming renewal (so the renewal will take place even if the customer opts out of auto-renewal before the
            end of the period)
             Example: will_renew.
        status (SubscriptionStatus): The status of a subscription. Please note that additional states might be added in
            the future. To determine whether or not a subscription currently provides access to any associated entitlements,
            use the _gives_access_ field.<br><br>Possible values:<br>• `trialing`: the subscription is in a free trial
            period<br>• `active`: the subscription is active, in a paid period<br>• `expired`: the subscription is expired
            and no longer active<br>• `in_grace_period`: the subscription is past its regular expiry date and experienced a
            billing issue, but is currently still in an access-granting grace period<br>• `in_billing_retry`: the
            subscription has experienced a billing issue. Billing is being retried, access is suspended.-paused: the
            subscription is currently paused and should not provide access.<br>• `unknown`: the subscription is in an
            unknown state. Refer to the _gives_access_ field to determine whether or not to grant access.<br>• `incomplete`:
            the subscription is in an incomplete state, maybe due to incorrect billing details or because it's scheduled to
            start in the future.
             Example: trialing.
        total_revenue_in_usd (MonetaryAmount):
        presented_offering_id (Union[None, str]): The ID of the offering the customer saw when purchasing the
            subscription Example: ofrnge1a2b3c4d5.
        entitlements (SubscriptionEntitlementList):
        environment (Environment): The store environment Example: production.
        store (SubscriptionStore): Store the subscription belongs to Example: amazon.
        store_subscription_identifier (str): The subscription identifier as per the store (e.g, for Apple App Store, the
            `transaction_id` of the latest transaction of the subscription, or for Google Play Store, the Order ID of the
            last renewal of the subscription) Example: 12345678.
        ownership (Ownership):  Example: purchased.
        management_url (Union[None, str]): The URL to manage the subscription Example:
            https://apps.apple.com/account/subscriptions.
        pending_changes (Union['SubscriptionPendingChangesType0', None, Unset]): Indicates pending product changes.
            Present if the `auto_renewal_status` is `will_change_product`.
        country (Union[Unset, Any]): Billing country in ISO alpha 2 code
    """

    object_: SubscriptionObject
    id: str
    customer_id: str
    original_customer_id: str
    product_id: Union[None, str]
    starts_at: int
    current_period_starts_at: int
    current_period_ends_at: Union[None, int]
    gives_access: bool
    pending_payment: bool
    auto_renewal_status: SubscriptionAutoRenewalStatus
    status: SubscriptionStatus
    total_revenue_in_usd: "MonetaryAmount"
    presented_offering_id: Union[None, str]
    entitlements: "SubscriptionEntitlementList"
    environment: Environment
    store: SubscriptionStore
    store_subscription_identifier: str
    ownership: Ownership
    management_url: Union[None, str]
    pending_changes: Union["SubscriptionPendingChangesType0", None, Unset] = UNSET
    country: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.subscription_pending_changes_type_0 import (
            SubscriptionPendingChangesType0,
        )

        object_ = self.object_.value

        id = self.id

        customer_id = self.customer_id

        original_customer_id = self.original_customer_id

        product_id: Union[None, str]
        product_id = self.product_id

        starts_at = self.starts_at

        current_period_starts_at = self.current_period_starts_at

        current_period_ends_at: Union[None, int]
        current_period_ends_at = self.current_period_ends_at

        gives_access = self.gives_access

        pending_payment = self.pending_payment

        auto_renewal_status = self.auto_renewal_status.value

        status = self.status.value

        total_revenue_in_usd = self.total_revenue_in_usd.to_dict()

        presented_offering_id: Union[None, str]
        presented_offering_id = self.presented_offering_id

        entitlements = self.entitlements.to_dict()

        environment = self.environment.value

        store = self.store.value

        store_subscription_identifier = self.store_subscription_identifier

        ownership = self.ownership.value

        management_url: Union[None, str]
        management_url = self.management_url

        pending_changes: Union[Dict[str, Any], None, Unset]
        if isinstance(self.pending_changes, Unset):
            pending_changes = UNSET
        elif isinstance(self.pending_changes, SubscriptionPendingChangesType0):
            pending_changes = self.pending_changes.to_dict()
        else:
            pending_changes = self.pending_changes

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "customer_id": customer_id,
                "original_customer_id": original_customer_id,
                "product_id": product_id,
                "starts_at": starts_at,
                "current_period_starts_at": current_period_starts_at,
                "current_period_ends_at": current_period_ends_at,
                "gives_access": gives_access,
                "pending_payment": pending_payment,
                "auto_renewal_status": auto_renewal_status,
                "status": status,
                "total_revenue_in_usd": total_revenue_in_usd,
                "presented_offering_id": presented_offering_id,
                "entitlements": entitlements,
                "environment": environment,
                "store": store,
                "store_subscription_identifier": store_subscription_identifier,
                "ownership": ownership,
                "management_url": management_url,
            }
        )
        if pending_changes is not UNSET:
            field_dict["pending_changes"] = pending_changes
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.monetary_amount import MonetaryAmount
        from ..models.subscription_entitlement_list import SubscriptionEntitlementList
        from ..models.subscription_pending_changes_type_0 import (
            SubscriptionPendingChangesType0,
        )

        d = src_dict.copy()
        object_ = SubscriptionObject(d.pop("object"))

        id = d.pop("id")

        customer_id = d.pop("customer_id")

        original_customer_id = d.pop("original_customer_id")

        def _parse_product_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        product_id = _parse_product_id(d.pop("product_id"))

        starts_at = d.pop("starts_at")

        current_period_starts_at = d.pop("current_period_starts_at")

        def _parse_current_period_ends_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        current_period_ends_at = _parse_current_period_ends_at(
            d.pop("current_period_ends_at")
        )

        gives_access = d.pop("gives_access")

        pending_payment = d.pop("pending_payment")

        auto_renewal_status = SubscriptionAutoRenewalStatus(
            d.pop("auto_renewal_status")
        )

        status = SubscriptionStatus(d.pop("status"))

        total_revenue_in_usd = MonetaryAmount.from_dict(d.pop("total_revenue_in_usd"))

        def _parse_presented_offering_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        presented_offering_id = _parse_presented_offering_id(
            d.pop("presented_offering_id")
        )

        entitlements = SubscriptionEntitlementList.from_dict(d.pop("entitlements"))

        environment = Environment(d.pop("environment"))

        store = SubscriptionStore(d.pop("store"))

        store_subscription_identifier = d.pop("store_subscription_identifier")

        ownership = Ownership(d.pop("ownership"))

        def _parse_management_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        management_url = _parse_management_url(d.pop("management_url"))

        def _parse_pending_changes(
            data: object,
        ) -> Union["SubscriptionPendingChangesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pending_changes_type_0 = SubscriptionPendingChangesType0.from_dict(data)

                return pending_changes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SubscriptionPendingChangesType0", None, Unset], data)

        pending_changes = _parse_pending_changes(d.pop("pending_changes", UNSET))

        country = d.pop("country", UNSET)

        subscription = cls(
            object_=object_,
            id=id,
            customer_id=customer_id,
            original_customer_id=original_customer_id,
            product_id=product_id,
            starts_at=starts_at,
            current_period_starts_at=current_period_starts_at,
            current_period_ends_at=current_period_ends_at,
            gives_access=gives_access,
            pending_payment=pending_payment,
            auto_renewal_status=auto_renewal_status,
            status=status,
            total_revenue_in_usd=total_revenue_in_usd,
            presented_offering_id=presented_offering_id,
            entitlements=entitlements,
            environment=environment,
            store=store,
            store_subscription_identifier=store_subscription_identifier,
            ownership=ownership,
            management_url=management_url,
            pending_changes=pending_changes,
            country=country,
        )

        subscription.additional_properties = d
        return subscription

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
