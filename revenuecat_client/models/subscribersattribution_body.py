from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subscribersattribution_body_network import (
    SubscribersattributionBodyNetwork,
)

if TYPE_CHECKING:
    from ..models.subscribersattribution_body_data import SubscribersattributionBodyData


T = TypeVar("T", bound="SubscribersattributionBody")


@_attrs_define
class SubscribersattributionBody:
    """
    Attributes:
        data (SubscribersattributionBodyData): The data returned by the attribution network callbacks.
        network (SubscribersattributionBodyNetwork): The attribution network the data is coming from. See below for
            possible values.
    """

    data: "SubscribersattributionBodyData"
    network: SubscribersattributionBodyNetwork
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        network = self.network.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "network": network,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.subscribersattribution_body_data import (
            SubscribersattributionBodyData,
        )

        d = src_dict.copy()
        data = SubscribersattributionBodyData.from_dict(d.pop("data"))

        network = SubscribersattributionBodyNetwork(d.pop("network"))

        subscribersattribution_body = cls(
            data=data,
            network=network,
        )

        subscribersattribution_body.additional_properties = d
        return subscribersattribution_body

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
