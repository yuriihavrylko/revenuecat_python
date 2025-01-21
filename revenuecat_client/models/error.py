from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_object import ErrorObject
from ..models.error_type import ErrorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        object_ (ErrorObject): String representing the object's type. Objects of the same type share the same value.
            Example: error.
        type (ErrorType): The error type Example: parameter_error.
        message (str): A message describing the reason of the error Example: id shouldn't be longer than 1,500
            characters.
        retryable (bool): Indicates if the error is retryable or not
        param (Union[None, Unset, str]): If the error is parameter-specific, the parameter related to the error Example:
            customer_id.
        doc_url (Union[Unset, str]): A URL to more information about the error reported Example:
            https://errors.rev.cat/parameter-error.
        backoff_ms (Union[None, Unset, int]): The ms the client should wait before retrying the request. Only present
            for retryable errors.
    """

    object_: ErrorObject
    type: ErrorType
    message: str
    retryable: bool
    param: Union[None, Unset, str] = UNSET
    doc_url: Union[Unset, str] = UNSET
    backoff_ms: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        type = self.type.value

        message = self.message

        retryable = self.retryable

        param: Union[None, Unset, str]
        if isinstance(self.param, Unset):
            param = UNSET
        else:
            param = self.param

        doc_url = self.doc_url

        backoff_ms: Union[None, Unset, int]
        if isinstance(self.backoff_ms, Unset):
            backoff_ms = UNSET
        else:
            backoff_ms = self.backoff_ms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "type": type,
                "message": message,
                "retryable": retryable,
            }
        )
        if param is not UNSET:
            field_dict["param"] = param
        if doc_url is not UNSET:
            field_dict["doc_url"] = doc_url
        if backoff_ms is not UNSET:
            field_dict["backoff_ms"] = backoff_ms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = ErrorObject(d.pop("object"))

        type = ErrorType(d.pop("type"))

        message = d.pop("message")

        retryable = d.pop("retryable")

        def _parse_param(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        param = _parse_param(d.pop("param", UNSET))

        doc_url = d.pop("doc_url", UNSET)

        def _parse_backoff_ms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backoff_ms = _parse_backoff_ms(d.pop("backoff_ms", UNSET))

        error = cls(
            object_=object_,
            type=type,
            message=message,
            retryable=retryable,
            param=param,
            doc_url=doc_url,
            backoff_ms=backoff_ms,
        )

        error.additional_properties = d
        return error

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
