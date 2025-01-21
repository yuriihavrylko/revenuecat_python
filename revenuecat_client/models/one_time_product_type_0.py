from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OneTimeProductType0")


@_attrs_define
class OneTimeProductType0:
    """
    Attributes:
        is_consumable (Union[None, bool]): Indicates whether the product is consumable or not. Example: True.
    """

    is_consumable: Union[None, bool]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_consumable: Union[None, bool]
        is_consumable = self.is_consumable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_consumable": is_consumable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_is_consumable(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        is_consumable = _parse_is_consumable(d.pop("is_consumable"))

        one_time_product_type_0 = cls(
            is_consumable=is_consumable,
        )

        one_time_product_type_0.additional_properties = d
        return one_time_product_type_0

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
