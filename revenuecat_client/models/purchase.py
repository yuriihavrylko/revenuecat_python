from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment import Environment
from ..models.ownership import Ownership
from ..models.purchase_object import PurchaseObject
from ..models.purchase_status import PurchaseStatus
from ..models.purchase_store import PurchaseStore
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monetary_amount import MonetaryAmount
    from ..models.purchase_entitlement_list import PurchaseEntitlementList


T = TypeVar("T", bound="Purchase")


@_attrs_define
class Purchase:
    """
    Attributes:
        object_ (PurchaseObject): String representing the object's type. Objects of the same type share the same value.
        id (str): The id of the purchase Example: purch1a2b3c4d5e.
        customer_id (str): The id of the customer Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        original_customer_id (str): The ID of the original customer Example: 19b8de26-77c1-49f1-aa18-019a391603e2.
        product_id (str): The ID of the product that was purchased Example: prod1a2b3c4d5e.
        purchased_at (int): The date when the purchase was made in ms since epoch Example: 1658399423658.
        revenue_in_usd (MonetaryAmount):
        quantity (int): The quantity of the product purchased in one transaction Example: 1.
        status (PurchaseStatus): The status of a purchase Example: owned.
        presented_offering_id (Union[None, str]): The ID of the offering the customer saw when they did the purchase
            Example: ofrnge1a2b3c4d5.
        entitlements (PurchaseEntitlementList):
        environment (Environment): The store environment Example: production.
        store (PurchaseStore): Store the purchase belongs to Example: amazon.
        store_purchase_identifier (str): The store purchase identifier Example: 12345678.
        ownership (Ownership):  Example: purchased.
        country (Union[Unset, Any]): Billing country in ISO alpha 2 code
    """

    object_: PurchaseObject
    id: str
    customer_id: str
    original_customer_id: str
    product_id: str
    purchased_at: int
    revenue_in_usd: "MonetaryAmount"
    quantity: int
    status: PurchaseStatus
    presented_offering_id: Union[None, str]
    entitlements: "PurchaseEntitlementList"
    environment: Environment
    store: PurchaseStore
    store_purchase_identifier: str
    ownership: Ownership
    country: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        customer_id = self.customer_id

        original_customer_id = self.original_customer_id

        product_id = self.product_id

        purchased_at = self.purchased_at

        revenue_in_usd = self.revenue_in_usd.to_dict()

        quantity = self.quantity

        status = self.status.value

        presented_offering_id: Union[None, str]
        presented_offering_id = self.presented_offering_id

        entitlements = self.entitlements.to_dict()

        environment = self.environment.value

        store = self.store.value

        store_purchase_identifier = self.store_purchase_identifier

        ownership = self.ownership.value

        country = self.country

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "customer_id": customer_id,
                "original_customer_id": original_customer_id,
                "product_id": product_id,
                "purchased_at": purchased_at,
                "revenue_in_usd": revenue_in_usd,
                "quantity": quantity,
                "status": status,
                "presented_offering_id": presented_offering_id,
                "entitlements": entitlements,
                "environment": environment,
                "store": store,
                "store_purchase_identifier": store_purchase_identifier,
                "ownership": ownership,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.monetary_amount import MonetaryAmount
        from ..models.purchase_entitlement_list import PurchaseEntitlementList

        d = src_dict.copy()
        object_ = PurchaseObject(d.pop("object"))

        id = d.pop("id")

        customer_id = d.pop("customer_id")

        original_customer_id = d.pop("original_customer_id")

        product_id = d.pop("product_id")

        purchased_at = d.pop("purchased_at")

        revenue_in_usd = MonetaryAmount.from_dict(d.pop("revenue_in_usd"))

        quantity = d.pop("quantity")

        status = PurchaseStatus(d.pop("status"))

        def _parse_presented_offering_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        presented_offering_id = _parse_presented_offering_id(
            d.pop("presented_offering_id")
        )

        entitlements = PurchaseEntitlementList.from_dict(d.pop("entitlements"))

        environment = Environment(d.pop("environment"))

        store = PurchaseStore(d.pop("store"))

        store_purchase_identifier = d.pop("store_purchase_identifier")

        ownership = Ownership(d.pop("ownership"))

        country = d.pop("country", UNSET)

        purchase = cls(
            object_=object_,
            id=id,
            customer_id=customer_id,
            original_customer_id=original_customer_id,
            product_id=product_id,
            purchased_at=purchased_at,
            revenue_in_usd=revenue_in_usd,
            quantity=quantity,
            status=status,
            presented_offering_id=presented_offering_id,
            entitlements=entitlements,
            environment=environment,
            store=store,
            store_purchase_identifier=store_purchase_identifier,
            ownership=ownership,
            country=country,
        )

        purchase.additional_properties = d
        return purchase

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
