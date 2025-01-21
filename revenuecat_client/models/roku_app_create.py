from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roku_app_create_roku_type_0 import RokuAppCreateRokuType0


T = TypeVar("T", bound="RokuAppCreate")


@_attrs_define
class RokuAppCreate:
    """
    Attributes:
        roku (Union['RokuAppCreateRokuType0', None, Unset]): Roku Channel Store details. Should only be used when type
            is roku.
    """

    roku: Union["RokuAppCreateRokuType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.roku_app_create_roku_type_0 import RokuAppCreateRokuType0

        roku: Union[Dict[str, Any], None, Unset]
        if isinstance(self.roku, Unset):
            roku = UNSET
        elif isinstance(self.roku, RokuAppCreateRokuType0):
            roku = self.roku.to_dict()
        else:
            roku = self.roku

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if roku is not UNSET:
            field_dict["roku"] = roku

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.roku_app_create_roku_type_0 import RokuAppCreateRokuType0

        d = src_dict.copy()

        def _parse_roku(data: object) -> Union["RokuAppCreateRokuType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                roku_type_0 = RokuAppCreateRokuType0.from_dict(data)

                return roku_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RokuAppCreateRokuType0", None, Unset], data)

        roku = _parse_roku(d.pop("roku", UNSET))

        roku_app_create = cls(
            roku=roku,
        )

        roku_app_create.additional_properties = d
        return roku_app_create

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
