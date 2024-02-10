from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriberSubscriberSubscriptionsAnnual")


@_attrs_define
class SubscriberSubscriberSubscriptionsAnnual:
    """
    Attributes:
        auto_resume_date (Union[Unset, Any]):
        billing_issues_detected_at (Union[Unset, Any]):
        expires_date (Union[Unset, str]):  Example: 2019-08-14T21:07:40Z.
        grace_period_expires_date (Union[Unset, Any]):
        is_sandbox (Union[Unset, bool]):  Default: True. Example: True.
        original_purchase_date (Union[Unset, str]):  Example: 2019-02-21T00:42:05Z.
        ownership_type (Union[Unset, str]):  Example: PURCHASED.
        period_type (Union[Unset, str]):  Example: normal.
        purchase_date (Union[Unset, str]):  Example: 2019-07-14T20:07:40Z.
        refunded_at (Union[Unset, Any]):
        store (Union[Unset, str]):  Example: app_store.
        unsubscribe_detected_at (Union[Unset, str]):  Example: 2019-07-17T22:48:38Z.
    """

    auto_resume_date: Union[Unset, Any] = UNSET
    billing_issues_detected_at: Union[Unset, Any] = UNSET
    expires_date: Union[Unset, str] = UNSET
    grace_period_expires_date: Union[Unset, Any] = UNSET
    is_sandbox: Union[Unset, bool] = True
    original_purchase_date: Union[Unset, str] = UNSET
    ownership_type: Union[Unset, str] = UNSET
    period_type: Union[Unset, str] = UNSET
    purchase_date: Union[Unset, str] = UNSET
    refunded_at: Union[Unset, Any] = UNSET
    store: Union[Unset, str] = UNSET
    unsubscribe_detected_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_resume_date = self.auto_resume_date

        billing_issues_detected_at = self.billing_issues_detected_at

        expires_date = self.expires_date

        grace_period_expires_date = self.grace_period_expires_date

        is_sandbox = self.is_sandbox

        original_purchase_date = self.original_purchase_date

        ownership_type = self.ownership_type

        period_type = self.period_type

        purchase_date = self.purchase_date

        refunded_at = self.refunded_at

        store = self.store

        unsubscribe_detected_at = self.unsubscribe_detected_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_resume_date is not UNSET:
            field_dict["auto_resume_date"] = auto_resume_date
        if billing_issues_detected_at is not UNSET:
            field_dict["billing_issues_detected_at"] = billing_issues_detected_at
        if expires_date is not UNSET:
            field_dict["expires_date"] = expires_date
        if grace_period_expires_date is not UNSET:
            field_dict["grace_period_expires_date"] = grace_period_expires_date
        if is_sandbox is not UNSET:
            field_dict["is_sandbox"] = is_sandbox
        if original_purchase_date is not UNSET:
            field_dict["original_purchase_date"] = original_purchase_date
        if ownership_type is not UNSET:
            field_dict["ownership_type"] = ownership_type
        if period_type is not UNSET:
            field_dict["period_type"] = period_type
        if purchase_date is not UNSET:
            field_dict["purchase_date"] = purchase_date
        if refunded_at is not UNSET:
            field_dict["refunded_at"] = refunded_at
        if store is not UNSET:
            field_dict["store"] = store
        if unsubscribe_detected_at is not UNSET:
            field_dict["unsubscribe_detected_at"] = unsubscribe_detected_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_resume_date = d.pop("auto_resume_date", UNSET)

        billing_issues_detected_at = d.pop("billing_issues_detected_at", UNSET)

        expires_date = d.pop("expires_date", UNSET)

        grace_period_expires_date = d.pop("grace_period_expires_date", UNSET)

        is_sandbox = d.pop("is_sandbox", UNSET)

        original_purchase_date = d.pop("original_purchase_date", UNSET)

        ownership_type = d.pop("ownership_type", UNSET)

        period_type = d.pop("period_type", UNSET)

        purchase_date = d.pop("purchase_date", UNSET)

        refunded_at = d.pop("refunded_at", UNSET)

        store = d.pop("store", UNSET)

        unsubscribe_detected_at = d.pop("unsubscribe_detected_at", UNSET)

        subscriber_subscriber_subscriptions_annual = cls(
            auto_resume_date=auto_resume_date,
            billing_issues_detected_at=billing_issues_detected_at,
            expires_date=expires_date,
            grace_period_expires_date=grace_period_expires_date,
            is_sandbox=is_sandbox,
            original_purchase_date=original_purchase_date,
            ownership_type=ownership_type,
            period_type=period_type,
            purchase_date=purchase_date,
            refunded_at=refunded_at,
            store=store,
            unsubscribe_detected_at=unsubscribe_detected_at,
        )

        subscriber_subscriber_subscriptions_annual.additional_properties = d
        return subscriber_subscriber_subscriptions_annual

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
