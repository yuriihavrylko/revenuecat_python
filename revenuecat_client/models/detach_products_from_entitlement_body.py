from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DetachProductsFromEntitlementBody")


@_attrs_define
class DetachProductsFromEntitlementBody:
    """
    Attributes:
        product_ids (List[str]): IDs of the products to be detached from the entitlement.
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

        detach_products_from_entitlement_body = cls(
            product_ids=product_ids,
        )

        return detach_products_from_entitlement_body
