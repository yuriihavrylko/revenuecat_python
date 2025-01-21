from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="DetachProductsFromPackageBody")


@_attrs_define
class DetachProductsFromPackageBody:
    """
    Attributes:
        product_ids (List[str]): IDs of the products to detach from the package
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

        detach_products_from_package_body = cls(
            product_ids=product_ids,
        )

        return detach_products_from_package_body
