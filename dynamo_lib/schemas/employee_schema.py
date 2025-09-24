from .company_shift_schema import CompanyShiftSchema
from pydantic import Field, field_validator
from typing import Any, Dict, Optional
import json


class EmployeeSchema(CompanyShiftSchema):
    _update_intervals = False
    token_google_calendar: Optional[Dict[str, Any]] = Field(
        default_factory=dict, alias="token_google_calendar"
    )
    id: int = Field(default=0, alias="employee_id")
    name: str = Field(default="", alias="employee_name")
    services: list[int] = Field(default_factory=list, alias="employee_services")

    @field_validator("token_google_calendar", mode="before")
    @classmethod
    def convert_token_google_calendar_to_dict(
        cls, v: str | Dict[str, Any]
    ) -> Dict[str, Any]:
        if not v:
            return {}
        return json.loads(v) if isinstance(v, str) else v
