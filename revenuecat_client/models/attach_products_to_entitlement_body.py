from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttachProductsToEntitlementBody")


@_attrs_define
class AttachProductsToEntitlementBody:
    """
    Attributes:
        product_ids (List[str]): IDs of the products to be attached to the entitlement.
    """

    product_ids: List[str]

    def to_dict(self) -> Dict[str, Any]:
        product_ids = self.product_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "product_ids": product_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_ids = cast(List[str], d.pop("product_ids"))

        attach_products_to_entitlement_body = cls(
            product_ids=product_ids,
        )

        return attach_products_to_entitlement_body
