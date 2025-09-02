from ..core.enums import ControlStatus, EmpresaPlan
from pydantic import BaseModel, Field


class ControlSchema(BaseModel):
    company_identification: str = Field(
        default="", alias="company_identification", description="Company identification"
    )

    employee_limit: int = Field(
        default=0, alias="employee_limit", description="Limit of employees"
    )

    phone_id: int = Field(default=0, alias="phone_id", description="Phone ID")

    token_openai: str = Field(
        default="", alias="token_openai", description="OpenAI token"
    )

    plan: EmpresaPlan = Field(
        default=EmpresaPlan.BASIC, alias="plan", description="Company plan"
    )

    status: ControlStatus = Field(
        default=ControlStatus.OKAY, alias="status", description="Company status"
    )

    beta_tester: bool = Field(
        default=False, alias="beta_tester", description="Is the company a beta tester?"
    )

    has_send_off: bool = Field(
        default=False,
        alias="has_send_off",
        description="Does the company have send-off feature?",
    )

    is_evolution: bool = Field(
        default=False, alias="is_evolution", description="Is using the evolution api?"
    )

    is_uazapi: bool = Field(
        default=False, alias="is_uazapi", description="Is using the uazapi api?"
    )
    session_id: str = Field(default="0", alias="session_id", description="Session ID")
