from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eligibility_criteria import EligibilityCriteria

if TYPE_CHECKING:
    from ..models.product import Product


T = TypeVar("T", bound="PackageProductAssociation")


@_attrs_define
class PackageProductAssociation:
    """
    Attributes:
        product (Product):
        eligibility_criteria (EligibilityCriteria):
    """

    product: "Product"
    eligibility_criteria: EligibilityCriteria
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product = self.product.to_dict()

        eligibility_criteria = self.eligibility_criteria.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product": product,
                "eligibility_criteria": eligibility_criteria,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product import Product

        d = src_dict.copy()
        product = Product.from_dict(d.pop("product"))

        eligibility_criteria = EligibilityCriteria(d.pop("eligibility_criteria"))

        package_product_association = cls(
            product=product,
            eligibility_criteria=eligibility_criteria,
        )

        package_product_association.additional_properties = d
        return package_product_association

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
