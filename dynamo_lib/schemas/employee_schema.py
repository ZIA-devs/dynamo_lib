from .company_shift_schema import CompanyShiftSchema
from pydantic import Field
from typing import Any


class EmployeeSchema(CompanyShiftSchema):
    _update_intervals = False
    token_google_calendar: dict[str, Any] = Field(default_factory=dict, alias='token_google_calendar', description='Calendar token for the employee')
    id: int = Field(default=0, alias='employee_id', description='ID of the employee')
    name: str = Field(default='', alias='employee_name', description='Name of the employee')
    services:list[int] = Field(default_factory=list, alias='employee_services', description='List of service IDs offered by the employee')
