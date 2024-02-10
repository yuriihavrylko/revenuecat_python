from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_subscriber_attributes_response_400_attribute_errors_item import (
        UpdateSubscriberAttributesResponse400AttributeErrorsItem,
    )


T = TypeVar("T", bound="UpdateSubscriberAttributesResponse400")


@_attrs_define
class UpdateSubscriberAttributesResponse400:
    """
    Attributes:
        code (Union[Unset, int]):  Default: 0. Example: 7263.
        message (Union[Unset, str]):  Example: Some subscriber attributes keys were unable to saved..
        attribute_errors (Union[Unset, List['UpdateSubscriberAttributesResponse400AttributeErrorsItem']]):
    """

    code: Union[Unset, int] = 0
    message: Union[Unset, str] = UNSET
    attribute_errors: Union[
        Unset, List["UpdateSubscriberAttributesResponse400AttributeErrorsItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        message = self.message

        attribute_errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attribute_errors, Unset):
            attribute_errors = []
            for attribute_errors_item_data in self.attribute_errors:
                attribute_errors_item = attribute_errors_item_data.to_dict()
                attribute_errors.append(attribute_errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if attribute_errors is not UNSET:
            field_dict["attribute_errors"] = attribute_errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_subscriber_attributes_response_400_attribute_errors_item import (
            UpdateSubscriberAttributesResponse400AttributeErrorsItem,
        )

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        attribute_errors = []
        _attribute_errors = d.pop("attribute_errors", UNSET)
        for attribute_errors_item_data in _attribute_errors or []:
            attribute_errors_item = (
                UpdateSubscriberAttributesResponse400AttributeErrorsItem.from_dict(
                    attribute_errors_item_data
                )
            )

            attribute_errors.append(attribute_errors_item)

        update_subscriber_attributes_response_400 = cls(
            code=code,
            message=message,
            attribute_errors=attribute_errors,
        )

        update_subscriber_attributes_response_400.additional_properties = d
        return update_subscriber_attributes_response_400

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
