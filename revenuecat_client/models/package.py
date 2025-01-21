from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.package_object import PackageObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_product_list import PackageProductList


T = TypeVar("T", bound="Package")


@_attrs_define
class Package:
    """
    Attributes:
        object_ (PackageObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the package Example: pkge1a2b3c4d5.
        lookup_key (str): The lookup_key of the package Example: monthly.
        display_name (str): The display name of the package Example: Monthly discounted with 3-day trial.
        position (Union[None, int]): The position of the package within the offering Example: 1.
        created_at (int): The date the package was created at in ms since epoch Example: 1658399423658.
        products (Union[Unset, PackageProductList]):
    """

    object_: PackageObject
    id: str
    lookup_key: str
    display_name: str
    position: Union[None, int]
    created_at: int
    products: Union[Unset, "PackageProductList"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        lookup_key = self.lookup_key

        display_name = self.display_name

        position: Union[None, int]
        position = self.position

        created_at = self.created_at

        products: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "lookup_key": lookup_key,
                "display_name": display_name,
                "position": position,
                "created_at": created_at,
            }
        )
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_product_list import PackageProductList

        d = src_dict.copy()
        object_ = PackageObject(d.pop("object"))

        id = d.pop("id")

        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        def _parse_position(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        _products = d.pop("products", UNSET)
        products: Union[Unset, PackageProductList]
        if isinstance(_products, Unset):
            products = UNSET
        else:
            products = PackageProductList.from_dict(_products)

        package = cls(
            object_=object_,
            id=id,
            lookup_key=lookup_key,
            display_name=display_name,
            position=position,
            created_at=created_at,
            products=products,
        )

        package.additional_properties = d
        return package

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
