from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateOfferingBody")


@_attrs_define
class UpdateOfferingBody:
    """
    Attributes:
        display_name (Union[Unset, str]): The display name of the offering Example: premium access to features.
        is_current (Union[Unset, bool]): Indicates if the offering is the current offering Example: True.
        metadata (Union[Unset, Any]): Custom metadata of the offering
    """

    display_name: Union[Unset, str] = UNSET
    is_current: Union[Unset, bool] = UNSET
    metadata: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name

        is_current = self.is_current

        metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        display_name = d.pop("display_name", UNSET)

        is_current = d.pop("is_current", UNSET)

        metadata = d.pop("metadata", UNSET)

        update_offering_body = cls(
            display_name=display_name,
            is_current=is_current,
            metadata=metadata,
        )

        return update_offering_body
