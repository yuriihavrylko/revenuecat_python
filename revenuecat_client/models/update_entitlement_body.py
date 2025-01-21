from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateEntitlementBody")


@_attrs_define
class UpdateEntitlementBody:
    """
    Attributes:
        display_name (str): The display name of the entitlement Example: Premium.
    """

    display_name: str

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name")

        update_entitlement_body = cls(
            display_name=display_name,
        )

        return update_entitlement_body
