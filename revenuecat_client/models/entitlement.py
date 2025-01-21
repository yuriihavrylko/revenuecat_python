from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entitlement_object import EntitlementObject
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entitlement_products_list import EntitlementProductsList


T = TypeVar("T", bound="Entitlement")


@_attrs_define
class Entitlement:
    """
    Attributes:
        object_ (EntitlementObject): String representing the object's type. Objects of the same type share the same
            value.
        project_id (str): ID of the project to which the entitlement belongs Example: proj1ab2c3d4.
        id (str): The id of the entitlement Example: entla1b2c3d4e5.
        lookup_key (str): A custom identifier of the entitlement Example: premium.
        display_name (str): The display name of the entitlement Example: Premium.
        created_at (int): The date when the entitlement was created in ms since epoch Example: 1658399423658.
        products (Union['EntitlementProductsList', None, Unset]): List of products attached to the entitlement
    """

    object_: EntitlementObject
    project_id: str
    id: str
    lookup_key: str
    display_name: str
    created_at: int
    products: Union["EntitlementProductsList", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.entitlement_products_list import EntitlementProductsList

        object_ = self.object_.value

        project_id = self.project_id

        id = self.id

        lookup_key = self.lookup_key

        display_name = self.display_name

        created_at = self.created_at

        products: Union[Dict[str, Any], None, Unset]
        if isinstance(self.products, Unset):
            products = UNSET
        elif isinstance(self.products, EntitlementProductsList):
            products = self.products.to_dict()
        else:
            products = self.products

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "project_id": project_id,
                "id": id,
                "lookup_key": lookup_key,
                "display_name": display_name,
                "created_at": created_at,
            }
        )
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entitlement_products_list import EntitlementProductsList

        d = src_dict.copy()
        object_ = EntitlementObject(d.pop("object"))

        project_id = d.pop("project_id")

        id = d.pop("id")

        lookup_key = d.pop("lookup_key")

        display_name = d.pop("display_name")

        created_at = d.pop("created_at")

        def _parse_products(
            data: object,
        ) -> Union["EntitlementProductsList", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                products_type_0 = EntitlementProductsList.from_dict(data)

                return products_type_0
            except:  # noqa: E722
                pass
            return cast(Union["EntitlementProductsList", None, Unset], data)

        products = _parse_products(d.pop("products", UNSET))

        entitlement = cls(
            object_=object_,
            project_id=project_id,
            id=id,
            lookup_key=lookup_key,
            display_name=display_name,
            created_at=created_at,
            products=products,
        )

        entitlement.additional_properties = d
        return entitlement

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
