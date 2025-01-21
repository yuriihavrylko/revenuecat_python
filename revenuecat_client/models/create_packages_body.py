from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePackagesBody")


@_attrs_define
class CreatePackagesBody:
    """
    Attributes:
        lookup_key (str): The lookup_key of the package Example: monthly.
        display_name (str): The display name of the package Example: monthly with one-week trial.
        position (Union[Unset, int]): The position of the package in the offering Example: 1.
    """

    lookup_key: str
    display_name: str
    position: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        lookup_key = self.lookup_key

        display_name = self.display_name

        position = self.position

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "lookup_key": lookup_key,
                "display_name": display_name,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        position = d.pop("position", UNSET)

        create_packages_body = cls(
            lookup_key=lookup_key,
            display_name=display_name,
            position=position,
        )

        return create_packages_body
