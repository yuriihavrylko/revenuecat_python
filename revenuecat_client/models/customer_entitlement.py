from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_entitlement_object import CustomerEntitlementObject

T = TypeVar("T", bound="CustomerEntitlement")


@_attrs_define
class CustomerEntitlement:
    """
    Attributes:
        object_ (CustomerEntitlementObject): String representing the object's type. Objects of the same type share the
            same value.
        entitlement_id (str): ID of the entitlement granted to the customer Example: entla1b2c3d4e5.
        expires_at (Union[None, int]): The date after which the access to the entitlement expires in ms since epoch
            Example: 1658399423658.
    """

    object_: CustomerEntitlementObject
    entitlement_id: str
    expires_at: Union[None, int]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        entitlement_id = self.entitlement_id

        expires_at: Union[None, int]
        expires_at = self.expires_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "entitlement_id": entitlement_id,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = CustomerEntitlementObject(d.pop("object"))

        entitlement_id = d.pop("entitlement_id")

        def _parse_expires_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        customer_entitlement = cls(
            object_=object_,
            entitlement_id=entitlement_id,
            expires_at=expires_at,
        )

        customer_entitlement.additional_properties = d
        return customer_entitlement

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
