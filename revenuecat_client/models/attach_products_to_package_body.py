from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.package_product_id_association import PackageProductIDAssociation


T = TypeVar("T", bound="AttachProductsToPackageBody")


@_attrs_define
class AttachProductsToPackageBody:
    """
    Attributes:
        products (List['PackageProductIDAssociation']): Product association list
    """

    products: List["PackageProductIDAssociation"]

    def to_dict(self) -> Dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_product_id_association import PackageProductIDAssociation

        d = src_dict.copy()
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = PackageProductIDAssociation.from_dict(products_item_data)

            products.append(products_item)

        attach_products_to_package_body = cls(
            products=products,
        )

        return attach_products_to_package_body
