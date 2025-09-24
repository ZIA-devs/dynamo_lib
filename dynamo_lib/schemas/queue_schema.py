from pydantic import BaseModel, Field


class QueueSchema(BaseModel):
    company_sk: str = Field(default="", alias="queue_company_sk")
    client_phone: str = Field(default="", alias="queue_client_phone")
    sector_id: int = Field(default=0, alias="queue_sector_id")
    sector_name: str = Field(default="", alias="queue_sector_name")
