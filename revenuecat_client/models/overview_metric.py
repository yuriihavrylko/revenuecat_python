import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.overview_metric_object import OverviewMetricObject
from ..models.overview_metric_period import OverviewMetricPeriod

T = TypeVar("T", bound="OverviewMetric")


@_attrs_define
class OverviewMetric:
    """
    Attributes:
        object_ (OverviewMetricObject): String representing the object's type. Objects of the same type share the same
            value.
        id (str): Id of the overview metric Example: active_trials.
        name (str): Display name of the overview metric Example: Active Trials.
        description (str): Description of the overview metric
        unit (str): Unit of the overview metric Example: $.
        period (OverviewMetricPeriod): Length of time during which metric data is collected in ISO 8601 format. Zero
            period means metric data was collected now Example: P0D.
        value (float): Value of the overview metric Example: 34765.
        last_updated_at (Union[None, int]): Last time the overview metric was updated in ms since epoch Example:
            1658399423658.
        last_updated_at_iso8601 (Union[None, datetime.datetime]): Last time the overview metric was updated datetime in
            ISO 8601 format Example: 2022-10-13 09:45:00.123000+00:00.
    """

    object_: OverviewMetricObject
    id: str
    name: str
    description: str
    unit: str
    period: OverviewMetricPeriod
    value: float
    last_updated_at: Union[None, int]
    last_updated_at_iso8601: Union[None, datetime.datetime]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        object_ = self.object_.value

        id = self.id

        name = self.name

        description = self.description

        unit = self.unit

        period = self.period.value

        value = self.value

        last_updated_at: Union[None, int]
        last_updated_at = self.last_updated_at

        last_updated_at_iso8601: Union[None, str]
        if isinstance(self.last_updated_at_iso8601, datetime.datetime):
            last_updated_at_iso8601 = self.last_updated_at_iso8601.isoformat()
        else:
            last_updated_at_iso8601 = self.last_updated_at_iso8601

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "id": id,
                "name": name,
                "description": description,
                "unit": unit,
                "period": period,
                "value": value,
                "last_updated_at": last_updated_at,
                "last_updated_at_iso8601": last_updated_at_iso8601,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        object_ = OverviewMetricObject(d.pop("object"))

        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        unit = d.pop("unit")

        period = OverviewMetricPeriod(d.pop("period"))

        value = d.pop("value")

        def _parse_last_updated_at(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        last_updated_at = _parse_last_updated_at(d.pop("last_updated_at"))

        def _parse_last_updated_at_iso8601(
            data: object,
        ) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_at_iso8601_type_0 = isoparse(data)

                return last_updated_at_iso8601_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated_at_iso8601 = _parse_last_updated_at_iso8601(
            d.pop("last_updated_at_iso8601")
        )

        overview_metric = cls(
            object_=object_,
            id=id,
            name=name,
            description=description,
            unit=unit,
            period=period,
            value=value,
            last_updated_at=last_updated_at,
            last_updated_at_iso8601=last_updated_at_iso8601,
        )

        overview_metric.additional_properties = d
        return overview_metric

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
