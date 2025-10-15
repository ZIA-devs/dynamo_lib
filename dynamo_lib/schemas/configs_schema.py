from ..core.enums import EmpresaPlan, EmpresaTipo
from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict, Optional, List
import json


class ConfigsSchema(BaseModel):
    assistant_id: str = Field(default="", alias="assistant_id")
    assistant_name: str = Field(default="", alias="assistant_name")
    business_type: EmpresaTipo = Field(
        default=EmpresaTipo.PADRAO, alias="business_type"
    )
    email: str = Field(default="", alias="email")
    company_name: str = Field(default="", alias="company_name")
    employee_limit: int = Field(default=99, alias="employee_limit")
    phone_id: str = Field(default="", alias="phone_id")
    plan: EmpresaPlan = Field(default=EmpresaPlan.SCHEDULE, alias="plan")
    take_in_conv_timeout: int = Field(default=3600, alias="take_in_conv_timeout")
    take_in_conv_start_warn: bool = Field(default=True, alias="take_in_conv_start_warn")
    take_in_conv_end_warn: bool = Field(default=True, alias="take_in_conv_end_warn")
    token_asa: str = Field(default="", alias="token_asa")
    token_olx: str = Field(default="", alias="token_olx")
    token_uazapi: str = Field(default="", alias="token_uazapi")
    token_google_calendar: Optional[Dict[str, Any]] = Field(
        default_factory=dict, alias="token_google_calendar"
    )
    token_openai: str = Field(default="", alias="token_openai")
    token_wpp: str = Field(default="", alias="token_wpp")
    waba_id: str = Field(default="", alias="waba_id")
    sector_timeout: int = Field(default=3600, alias="sector_timeout")
    beta_tester: bool = Field(default=False, alias="beta_tester")
    has_send_off: bool = Field(default=False, alias="has_send_off")
    has_multiple_msg_warn: bool = Field(default=True, alias="has_multiple_msg_warn")
    block_template_creation: bool = Field(
        default=False, alias="block_template_creation"
    )
    hide_assistant_name: bool = Field(default=False, alias="hide_assistant_name")
    olx_integration: bool = Field(default=False, alias="olx_integration")
    session_id: str = Field(default="0", alias="session_id")
    is_active: bool = Field(default=True, alias="is_active")
    test_numbers: List[str] = Field(default_factory=list, alias="test_numbers")

    @field_validator("phone_id", mode="before")
    @classmethod
    def convert_phone_id_to_str(cls, v: int | str) -> str:
        return str(v)

    @field_validator("token_google_calendar", mode="before")
    @classmethod
    def convert_token_google_calendar_to_dict(
        cls, v: str | Dict[str, Any]
    ) -> Dict[str, Any]:
        return json.loads(v) if isinstance(v, str) else v
