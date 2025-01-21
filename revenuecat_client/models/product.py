from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.product_object import ProductObject
from ..types import UNSET, Unset

T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        object_ (ProductObject): String representing the object's type. Objects of the same type share the same value.
            Always has the value `list`.
        id (str): The id of the product Example: prod1a2b3c4d5e.
        store_identifier (str): The store product identifier Example: rc_1w_199.
        type (Any): The product type
        created_at (int): The date when the product was created in ms since epoch Example: 1658399423658.
        app_id (str): The id of the app Example: app1a2b3c4.
        display_name (Union[None, str]): The display name of the product Example: Premium Monthly 2023.
        subscription (Union[Unset, Any]): The subscription product object
        one_time (Union[Unset, Any]): The one time product object
        app (Union[Unset, Any]): The app associated with the product
    """

    object_: ProductObject
    id: str
    store_identifier: str
    type: Any
    created_at: int
    app_id: str
    display_name: Union[None, str]
    subscription: Union[Unset, Any] = UNSET
    one_time: Union[Unset, Any] = UNSET
    app: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        store_identifier = self.store_identifier

        type = self.type

        created_at = self.created_at

        app_id = self.app_id

        display_name: Union[None, str]
        display_name = self.display_name

        subscription = self.subscription

        one_time = self.one_time

        app = self.app

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "store_identifier": store_identifier,
                "type": type,
                "created_at": created_at,
                "app_id": app_id,
                "display_name": display_name,
            }
        )
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if one_time is not UNSET:
            field_dict["one_time"] = one_time
        if app is not UNSET:
            field_dict["app"] = app

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = ProductObject(d.pop("object"))

        id = d.pop("id")

        store_identifier = d.pop("store_identifier")

        type = d.pop("type")

        created_at = d.pop("created_at")

        app_id = d.pop("app_id")

        def _parse_display_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        display_name = _parse_display_name(d.pop("display_name"))

        subscription = d.pop("subscription", UNSET)

        one_time = d.pop("one_time", UNSET)

        app = d.pop("app", UNSET)

        product = cls(
            object_=object_,
            id=id,
            store_identifier=store_identifier,
            type=type,
            created_at=created_at,
            app_id=app_id,
            display_name=display_name,
            subscription=subscription,
            one_time=one_time,
            app=app,
        )

        product.additional_properties = d
        return product

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
