from pydantic import BaseModel, Field


class ServiceSchema(BaseModel):
    cost: float = Field(default=0.0, alias="service_cost")
    duration: int = Field(default=90, alias="service_duration")
    id: int = Field(default=1, alias="service_id")
    name: str = Field(default="", alias="service_name")
