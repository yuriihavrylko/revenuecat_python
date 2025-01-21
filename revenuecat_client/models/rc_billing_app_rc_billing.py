from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rc_billing_currency import RCBillingCurrency
from ..types import UNSET, Unset

T = TypeVar("T", bound="RCBillingAppRcBilling")


@_attrs_define
class RCBillingAppRcBilling:
    """Revenue Cat Billing Store type details

    Attributes:
        seller_company_name (str): The company name.  This field is deprecated. Please, use `app_name` instead.
        default_currency (RCBillingCurrency): ISO 4217 currency code Example: USD.
        stripe_account_id (Union[None, Unset, str]): Stripe account connected to your RevenueCat account.
        app_name (Union[Unset, str]): Shown in checkout, emails, and receipts sent to customers.
        seller_company_support_email (Union[None, Unset, str]): The company support email. This field is deprecated.
            Please, use `support_email` instead.
        support_email (Union[None, Unset, str]): Used as the `reply to` address in all emails sent to customers, to
            allow them to receive support.
    """

    seller_company_name: str
    default_currency: RCBillingCurrency
    stripe_account_id: Union[None, Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    seller_company_support_email: Union[None, Unset, str] = UNSET
    support_email: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        seller_company_name = self.seller_company_name

        default_currency = self.default_currency.value

        stripe_account_id: Union[None, Unset, str]
        if isinstance(self.stripe_account_id, Unset):
            stripe_account_id = UNSET
        else:
            stripe_account_id = self.stripe_account_id

        app_name = self.app_name

        seller_company_support_email: Union[None, Unset, str]
        if isinstance(self.seller_company_support_email, Unset):
            seller_company_support_email = UNSET
        else:
            seller_company_support_email = self.seller_company_support_email

        support_email: Union[None, Unset, str]
        if isinstance(self.support_email, Unset):
            support_email = UNSET
        else:
            support_email = self.support_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "seller_company_name": seller_company_name,
                "default_currency": default_currency,
            }
        )
        if stripe_account_id is not UNSET:
            field_dict["stripe_account_id"] = stripe_account_id
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if seller_company_support_email is not UNSET:
            field_dict["seller_company_support_email"] = seller_company_support_email
        if support_email is not UNSET:
            field_dict["support_email"] = support_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        seller_company_name = d.pop("seller_company_name")

        default_currency = RCBillingCurrency(d.pop("default_currency"))

        def _parse_stripe_account_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stripe_account_id = _parse_stripe_account_id(d.pop("stripe_account_id", UNSET))

        app_name = d.pop("app_name", UNSET)

        def _parse_seller_company_support_email(
            data: object,
        ) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        seller_company_support_email = _parse_seller_company_support_email(
            d.pop("seller_company_support_email", UNSET)
        )

        def _parse_support_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        support_email = _parse_support_email(d.pop("support_email", UNSET))

        rc_billing_app_rc_billing = cls(
            seller_company_name=seller_company_name,
            default_currency=default_currency,
            stripe_account_id=stripe_account_id,
            app_name=app_name,
            seller_company_support_email=seller_company_support_email,
            support_email=support_email,
        )

        rc_billing_app_rc_billing.additional_properties = d
        return rc_billing_app_rc_billing

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
