from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.experiment_enrollment_type_0_object import ExperimentEnrollmentType0Object

T = TypeVar("T", bound="ExperimentEnrollmentType0")


@_attrs_define
class ExperimentEnrollmentType0:
    """
    Attributes:
        object_ (ExperimentEnrollmentType0Object): String representing the object's type. Objects of the same type share
            the same value.
        id (str):
        name (str):
        variant (str): The variant of the Experiment that the Customer was or is assigned to, where 'a' represents the
            Control, and 'b' represents the Treatment. Example: a.
    """

    object_: ExperimentEnrollmentType0Object
    id: str
    name: str
    variant: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        variant = self.variant

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "variant": variant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = ExperimentEnrollmentType0Object(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        variant = d.pop("variant")

        experiment_enrollment_type_0 = cls(
            object_=object_,
            id=id,
            name=name,
            variant=variant,
        )

        experiment_enrollment_type_0.additional_properties = d
        return experiment_enrollment_type_0

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
