from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rc_billing_app_rc_billing import RCBillingAppRcBilling


T = TypeVar("T", bound="RCBillingApp")


@_attrs_define
class RCBillingApp:
    """
    Attributes:
        rc_billing (Union[Unset, RCBillingAppRcBilling]): Revenue Cat Billing Store type details
    """

    rc_billing: Union[Unset, "RCBillingAppRcBilling"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rc_billing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rc_billing, Unset):
            rc_billing = self.rc_billing.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rc_billing is not UNSET:
            field_dict["rc_billing"] = rc_billing

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.rc_billing_app_rc_billing import RCBillingAppRcBilling

        d = src_dict.copy()
        _rc_billing = d.pop("rc_billing", UNSET)
        rc_billing: Union[Unset, RCBillingAppRcBilling]
        if isinstance(_rc_billing, Unset):
            rc_billing = UNSET
        else:
            rc_billing = RCBillingAppRcBilling.from_dict(_rc_billing)

        rc_billing_app = cls(
            rc_billing=rc_billing,
        )

        rc_billing_app.additional_properties = d
        return rc_billing_app

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
