from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amazon_app_create_amazon import AmazonAppCreateAmazon


T = TypeVar("T", bound="AmazonAppCreate")


@_attrs_define
class AmazonAppCreate:
    """
    Attributes:
        amazon (Union[Unset, AmazonAppCreateAmazon]): Amazon type details. Should only be used when type is amazon.
    """

    amazon: Union[Unset, "AmazonAppCreateAmazon"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amazon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.amazon, Unset):
            amazon = self.amazon.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amazon is not UNSET:
            field_dict["amazon"] = amazon

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_app_create_amazon import AmazonAppCreateAmazon

        d = src_dict.copy()
        _amazon = d.pop("amazon", UNSET)
        amazon: Union[Unset, AmazonAppCreateAmazon]
        if isinstance(_amazon, Unset):
            amazon = UNSET
        else:
            amazon = AmazonAppCreateAmazon.from_dict(_amazon)

        amazon_app_create = cls(
            amazon=amazon,
        )

        amazon_app_create.additional_properties = d
        return amazon_app_create

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
