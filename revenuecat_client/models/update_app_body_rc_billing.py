from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rc_billing_currency import RCBillingCurrency
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppBodyRcBilling")


@_attrs_define
class UpdateAppBodyRcBilling:
    """RevenueCat Billing type details. Should only be used when type is rc_billing.

    Attributes:
        stripe_account_id (Union[None, Unset, str]): It needs to be connected to your RevenueCat account. It can be
            omitted if you only have a single Stripe account connected to your RevenueCat account.
        app_name (Union[None, Unset, str]): Shown in checkout, emails, and receipts sent to customers.
        support_email (Union[None, Unset, str]): Used as the `reply to` address in all emails sent to customers, to
            allow them to receive support.  If you leave this field blank, your RevenueCat account email address will be
            used.
        default_currency (Union[Unset, RCBillingCurrency]): ISO 4217 currency code Example: USD.
    """

    stripe_account_id: Union[None, Unset, str] = UNSET
    app_name: Union[None, Unset, str] = UNSET
    support_email: Union[None, Unset, str] = UNSET
    default_currency: Union[Unset, RCBillingCurrency] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stripe_account_id: Union[None, Unset, str]
        if isinstance(self.stripe_account_id, Unset):
            stripe_account_id = UNSET
        else:
            stripe_account_id = self.stripe_account_id

        app_name: Union[None, Unset, str]
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        support_email: Union[None, Unset, str]
        if isinstance(self.support_email, Unset):
            support_email = UNSET
        else:
            support_email = self.support_email

        default_currency: Union[Unset, str] = UNSET
        if not isinstance(self.default_currency, Unset):
            default_currency = self.default_currency.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stripe_account_id is not UNSET:
            field_dict["stripe_account_id"] = stripe_account_id
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if support_email is not UNSET:
            field_dict["support_email"] = support_email
        if default_currency is not UNSET:
            field_dict["default_currency"] = default_currency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_stripe_account_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stripe_account_id = _parse_stripe_account_id(d.pop("stripe_account_id", UNSET))

        def _parse_app_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        app_name = _parse_app_name(d.pop("app_name", UNSET))

        def _parse_support_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        support_email = _parse_support_email(d.pop("support_email", UNSET))

        _default_currency = d.pop("default_currency", UNSET)
        default_currency: Union[Unset, RCBillingCurrency]
        if isinstance(_default_currency, Unset):
            default_currency = UNSET
        else:
            default_currency = RCBillingCurrency(_default_currency)

        update_app_body_rc_billing = cls(
            stripe_account_id=stripe_account_id,
            app_name=app_name,
            support_email=support_email,
            default_currency=default_currency,
        )

        update_app_body_rc_billing.additional_properties = d
        return update_app_body_rc_billing

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
