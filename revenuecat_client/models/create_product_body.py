from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProductBody")


@_attrs_define
class CreateProductBody:
    """
    Attributes:
        store_identifier (str): The store identifier of the product.
            - For Apple App Store products this is the product ID of the subscription or in-app product.
            - For Google's Play Store, it should follow the format 'productId:basePlanId' for subscription products and SKU
            for one-time purchase products.
            - For Stripe, the product identifier that always starts with "prod_"
            - For Amazon, if it's a subscription, the term SKU of the subscription. If it's a one-time purchase, the SKU of
            the product.
            - For Roku, this is the product identifier of the subscription or one-time purchase product.
             Example: com.revenuecat.magicweather.monthly.
        app_id (str): The ID of the app Example: app1a2b3c4.
        type (Any): The product type
        display_name (Union[None, Unset, str]): The display name of the product Example: Premium Monthly 2023.
    """

    store_identifier: str
    app_id: str
    type: Any
    display_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        store_identifier = self.store_identifier

        app_id = self.app_id

        type = self.type

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "store_identifier": store_identifier,
                "app_id": app_id,
                "type": type,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        store_identifier = d.pop("store_identifier")

        app_id = d.pop("app_id")

        type = d.pop("type")

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        create_product_body = cls(
            store_identifier=store_identifier,
            app_id=app_id,
            type=type,
            display_name=display_name,
        )

        return create_product_body
