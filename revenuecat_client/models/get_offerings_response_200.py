from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_offerings_response_200_offerings_item import (
        GetOfferingsResponse200OfferingsItem,
    )


T = TypeVar("T", bound="GetOfferingsResponse200")


@_attrs_define
class GetOfferingsResponse200:
    """
    Attributes:
        current_offering_id (Union[Unset, str]):  Example: default.
        offerings (Union[Unset, List['GetOfferingsResponse200OfferingsItem']]):
    """

    current_offering_id: Union[Unset, str] = UNSET
    offerings: Union[Unset, List["GetOfferingsResponse200OfferingsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_offering_id = self.current_offering_id

        offerings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.offerings, Unset):
            offerings = []
            for offerings_item_data in self.offerings:
                offerings_item = offerings_item_data.to_dict()
                offerings.append(offerings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_offering_id is not UNSET:
            field_dict["current_offering_id"] = current_offering_id
        if offerings is not UNSET:
            field_dict["offerings"] = offerings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_offerings_response_200_offerings_item import (
            GetOfferingsResponse200OfferingsItem,
        )

        d = src_dict.copy()
        current_offering_id = d.pop("current_offering_id", UNSET)

        offerings = []
        _offerings = d.pop("offerings", UNSET)
        for offerings_item_data in _offerings or []:
            offerings_item = GetOfferingsResponse200OfferingsItem.from_dict(
                offerings_item_data
            )

            offerings.append(offerings_item)

        get_offerings_response_200 = cls(
            current_offering_id=current_offering_id,
            offerings=offerings,
        )

        get_offerings_response_200.additional_properties = d
        return get_offerings_response_200

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
