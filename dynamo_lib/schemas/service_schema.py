from pydantic import BaseModel, Field


class ServiceSchema(BaseModel):
    cost: float = Field(
        default=0.0, alias="service_cost", description="Cost of the service"
    )

    duration: int = Field(
        default=90,
        alias="service_duration",
        description="Duration of the service in minutes",
    )

    id: int = Field(default=1, alias="service_id", description="ID of the service")

    name: str = Field(
        default="", alias="service_name", description="Name of the service"
    )
