from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.overview_metrics_object import OverviewMetricsObject

if TYPE_CHECKING:
    from ..models.overview_metric import OverviewMetric


T = TypeVar("T", bound="OverviewMetrics")


@_attrs_define
class OverviewMetrics:
    """
    Attributes:
        object_ (OverviewMetricsObject): String representing the object's type. Objects of the same type share the same
            value.
        metrics (List['OverviewMetric']): Details about each overview metric.
    """

    object_: OverviewMetricsObject
    metrics: List["OverviewMetric"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        metrics = []
        for metrics_item_data in self.metrics:
            metrics_item = metrics_item_data.to_dict()
            metrics.append(metrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "metrics": metrics,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.overview_metric import OverviewMetric

        d = src_dict.copy()
        object_ = OverviewMetricsObject(d.pop("object"))

        metrics = []
        _metrics = d.pop("metrics")
        for metrics_item_data in _metrics:
            metrics_item = OverviewMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        overview_metrics = cls(
            object_=object_,
            metrics=metrics,
        )

        overview_metrics.additional_properties = d
        return overview_metrics

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
