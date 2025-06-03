from pydantic import BaseModel, Field


class QueueSchema(BaseModel):
    company_sk: str = Field(default='', alias='queue_company_sk', description='Sorting key')
    client_phone: str = Field(default='', alias='queue_client_phone', description='Phone number of the client in the queue')
    sector_id: int = Field(default=0, alias='queue_sector_id', description='ID of the sector')
    sector_name: str = Field(default='', alias='queue_sector_name', description='Name of the sector')
