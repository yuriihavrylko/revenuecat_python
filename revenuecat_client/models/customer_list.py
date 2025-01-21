from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.customer_list_object import CustomerListObject

if TYPE_CHECKING:
    from ..models.customer import Customer


T = TypeVar("T", bound="CustomerList")


@_attrs_define
class CustomerList:
    """
    Attributes:
        object_ (CustomerListObject): String representing the object's type. Objects of the same type share the same
            value. Always has the value `list`.
        items (List['Customer']): Details about each object.
        next_page (Union[None, str]): URL to access the next page of the project's customers. If not present / null,
            there is no next page Example: /v2/projects/projec1a2b3c4d/customers?starting_after=223xx1100.
        url (str): The URL where this list can be accessed. Example: /v2/projects/projec1a2b3c4d/customers.
    """

    object_: CustomerListObject
    items: List["Customer"]
    next_page: Union[None, str]
    url: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_page: Union[None, str]
        next_page = self.next_page

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "items": items,
                "next_page": next_page,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.customer import Customer

        d = src_dict.copy()
        object_ = CustomerListObject(d.pop("object"))

        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = Customer.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_page(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_page = _parse_next_page(d.pop("next_page"))

        url = d.pop("url")

        customer_list = cls(
            object_=object_,
            items=items,
            next_page=next_page,
            url=url,
        )

        customer_list.additional_properties = d
        return customer_list

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
