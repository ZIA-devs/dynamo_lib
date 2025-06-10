from .company_shift_schema import CompanyShiftSchema
from pydantic import Field, field_validator
from typing import Any, Dict
import json


class EmployeeSchema(CompanyShiftSchema):
    _update_intervals = False

    token_google_calendar: Dict[str, Any] = Field(
        default_factory=dict,
        alias="token_google_calendar",
        description="Calendar token for the employee",
    )

    id: int = Field(default=0, alias="employee_id", description="ID of the employee")

    name: str = Field(
        default="", alias="employee_name", description="Name of the employee"
    )

    services: list[int] = Field(
        default_factory=list,
        alias="employee_services",
        description="List of service IDs offered by the employee",
    )

    @field_validator("token_google_calendar", mode="before")
    @classmethod
    def convert_token_google_calendar_to_dict(
        cls, v: str | Dict[str, Any]
    ) -> Dict[str, Any]:
        if not v:
            return {}
        return json.loads(v) if isinstance(v, str) else v
