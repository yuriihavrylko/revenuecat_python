from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_object import CustomerObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_active_entitlement_list import CustomerActiveEntitlementList
    from ..models.customer_attribute_list import CustomerAttributeList


T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        object_ (CustomerObject): String representing the object's type. Objects of the same type share the same value.
        id (str):  Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        project_id (str): ID of the project to which the customer belongs Example: proj1ab2c3d4.
        first_seen_at (int): The first time the customer was seen Example: 1658399423658.
        last_seen_at (Union[None, int]): The last time the customer was seen Example: 1658399423658.
        active_entitlements (Union[Unset, CustomerActiveEntitlementList]):
        experiment (Union[Unset, Any]): The experiment enrollment object
        attributes (Union[Unset, CustomerAttributeList]):
    """

    object_: CustomerObject
    id: str
    project_id: str
    first_seen_at: int
    last_seen_at: Union[None, int]
    active_entitlements: Union[Unset, "CustomerActiveEntitlementList"] = UNSET
    experiment: Union[Unset, Any] = UNSET
    attributes: Union[Unset, "CustomerAttributeList"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        project_id = self.project_id

        first_seen_at = self.first_seen_at

        last_seen_at: Union[None, int]
        last_seen_at = self.last_seen_at

        active_entitlements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_entitlements, Unset):
            active_entitlements = self.active_entitlements.to_dict()

        experiment = self.experiment

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "project_id": project_id,
                "first_seen_at": first_seen_at,
                "last_seen_at": last_seen_at,
            }
        )
        if active_entitlements is not UNSET:
            field_dict["active_entitlements"] = active_entitlements
        if experiment is not UNSET:
            field_dict["experiment"] = experiment
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer_active_entitlement_list import (
            CustomerActiveEntitlementList,
        )
        from ..models.customer_attribute_list import CustomerAttributeList

        d = src_dict.copy()
        object_ = CustomerObject(d.pop("object"))

        id = d.pop("id")

        project_id = d.pop("project_id")

        first_seen_at = d.pop("first_seen_at")

        def _parse_last_seen_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))

        _active_entitlements = d.pop("active_entitlements", UNSET)
        active_entitlements: Union[Unset, CustomerActiveEntitlementList]
        if isinstance(_active_entitlements, Unset):
            active_entitlements = UNSET
        else:
            active_entitlements = CustomerActiveEntitlementList.from_dict(
                _active_entitlements
            )

        experiment = d.pop("experiment", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, CustomerAttributeList]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CustomerAttributeList.from_dict(_attributes)

        customer = cls(
            object_=object_,
            id=id,
            project_id=project_id,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
            active_entitlements=active_entitlements,
            experiment=experiment,
            attributes=attributes,
        )

        customer.additional_properties = d
        return customer

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
