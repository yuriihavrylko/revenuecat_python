from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePackageBody")


@_attrs_define
class UpdatePackageBody:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name of the package Example: monthly with one-week trial.
        position (Union[Unset, int]): The position of the package within the offering Example: 2.
    """

    display_name: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name", UNSET)

        position = d.pop("position", UNSET)

        update_package_body = cls(
            display_name=display_name,
            position=position,
        )

        return update_package_body
