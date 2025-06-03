from pydantic import BaseModel, Field


class MainContactSchema(BaseModel):
    name: str = Field(default='', alias='main_contact_name', description='Name of the main contact')
    phone: str = Field(default='', alias='main_contact_phone', description='Phone number of the main contact')