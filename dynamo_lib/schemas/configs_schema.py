from ..core.enums import EmpresaPlan, EmpresaTipo
from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict, Optional
import json


class ConfigsSchema(BaseModel):
    assistant_id: str = Field(
        default="", alias="assistant_id", description="ID of the assistant"
    )

    assistant_name: str = Field(
        default="", alias="assistant_name", description="Name of the assistant"
    )

    business_type: EmpresaTipo = Field(
        default=EmpresaTipo.PADRAO,
        alias="business_type",
        description="Type of business",
    )

    email: str = Field(default="", alias="email", description="Email of the company")

    company_name: str = Field(
        default="", alias="company_name", description="Name of the company"
    )

    employee_limit: int = Field(
        default=99, alias="employee_limit", description="Limit of employees"
    )

    phone_id: str = Field(default="", alias="phone_id", description="ID of the phone")

    plan: EmpresaPlan = Field(
        default=EmpresaPlan.SCHEDULE, alias="plan", description="Plan of the company"
    )

    take_in_conv_timeout: int = Field(
        default=3600,
        alias="take_in_conv_timeout",
        description="Timeout for taking in conversation in seconds",
    )

    take_in_conv_start_warn: bool = Field(
        default=True,
        alias="take_in_conv_start_warn",
        description="Warn when starting to take in conversation",
    )

    take_in_conv_end_warn: bool = Field(
        default=True,
        alias="take_in_conv_end_warn",
        description="Warn when ending to take in conversation",
    )

    token_asa: str = Field(default="", alias="token_asa", description="ASA token")

    token_olx: str = Field(default="", alias="token_olx", description="OLX token")

    token_uazapi: str = Field(
        default="", alias="token_uazapi", description="Uazapi token"
    )

    token_google_calendar: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        alias="token_google_calendar",
        description="Google Calendar token",
    )

    token_openai: str = Field(
        default="", alias="token_openai", description="OpenAI token"
    )

    token_wpp: str = Field(default="", alias="token_wpp", description="WhatsApp token")

    waba_id: str = Field(
        default="", alias="waba_id", description="WhatsApp Business Account ID"
    )

    sector_timeout: int = Field(
        default=3600,
        alias="sector_timeout",
        description="Timeout for sector in seconds",
    )

    beta_tester: bool = Field(
        default=False, alias="beta_tester", description="Is a beta tester"
    )

    has_send_off: bool = Field(
        default=False, alias="has_send_off", description="Has send_off feature"
    )

    has_multiple_msg_warn: bool = Field(
        default=True,
        alias="has_multiple_msg_warn",
        description="Warn when multiple messages are sent",
    )

    block_template_creation: bool = Field(
        default=False,
        alias="block_template_creation",
        description="Block template creation",
    )
    hide_assistant_name: bool = Field(
        default=False,
        alias="hide_assistant_name",
        description="Hide assistant name in conversations",
    )
    olx_integration: bool = Field(
        default=False,
        alias="olx_integration",
        description="Enable OLX integration",
    )
    session_id: str = Field(
        default="0", alias="session_id", description="Session ID for the traeffik"
    )

    is_active: bool = Field(
        default=True, alias="is_active", description="Is the configuration active"
    )

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
