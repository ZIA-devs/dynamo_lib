from core.enums import ClientStatus
from pydantic import BaseModel, Field


class ClientSchema(BaseModel):
    last_msg: str = Field(default='', alias='client_last_msg', description='Last message from the client')
    name: str = Field(default='', alias='client_name', description='Name of the client')
    phone: str = Field(default='', alias='client_phone', description='Phone number of the client')
    sector_phone: str = Field(default='', alias='client_sector_phone', description='Sector phone number of the client')
    status: ClientStatus = Field(default=ClientStatus.ON_BOT, alias='client_status', description='Status of the client')
    thread: str = Field(default='', alias='client_thread', description='Thread ID of the client')
