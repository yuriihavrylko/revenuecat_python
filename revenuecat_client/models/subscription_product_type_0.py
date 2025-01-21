from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubscriptionProductType0")


@_attrs_define
class SubscriptionProductType0:
    """
    Attributes:
        duration (Union[None, str]): The duration of the subscription in ISO-8601 standard Example: P1M.
        grace_period_duration (Union[None, str]): The duration of the subscription's grace period in ISO-8601 standard
            Example: P3D.
        trial_duration (Union[None, str]): The duration of the subcription's trial period in ISO-8601 standard Example:
            P1W.
    """

    duration: Union[None, str]
    grace_period_duration: Union[None, str]
    trial_duration: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duration: Union[None, str]
        duration = self.duration

        grace_period_duration: Union[None, str]
        grace_period_duration = self.grace_period_duration

        trial_duration: Union[None, str]
        trial_duration = self.trial_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "grace_period_duration": grace_period_duration,
                "trial_duration": trial_duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_duration(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        duration = _parse_duration(d.pop("duration"))

        def _parse_grace_period_duration(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        grace_period_duration = _parse_grace_period_duration(
            d.pop("grace_period_duration")
        )

        def _parse_trial_duration(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        trial_duration = _parse_trial_duration(d.pop("trial_duration"))

        subscription_product_type_0 = cls(
            duration=duration,
            grace_period_duration=grace_period_duration,
            trial_duration=trial_duration,
        )

        subscription_product_type_0.additional_properties = d
        return subscription_product_type_0

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
