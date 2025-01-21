from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOfferingBody")


@_attrs_define
class CreateOfferingBody:
    """
    Attributes:
        lookup_key (str): The custom identifier of the offering Example: default.
        display_name (str): The display_name of the offering Example: The standard set of packages.
        metadata (Union[Unset, Any]): Custom metadata of the offering
    """

    lookup_key: str
    display_name: str
    metadata: Union[Unset, Any] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        lookup_key = self.lookup_key

        display_name = self.display_name

        metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "lookup_key": lookup_key,
                "display_name": display_name,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        metadata = d.pop("metadata", UNSET)

        create_offering_body = cls(
            lookup_key=lookup_key,
            display_name=display_name,
            metadata=metadata,
        )

        return create_offering_body
