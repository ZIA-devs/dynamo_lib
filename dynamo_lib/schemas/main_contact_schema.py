from pydantic import BaseModel, Field


class MainContactSchema(BaseModel):
    name: str = Field(default="", alias="main_contact_name")
    phone: str = Field(default="", alias="main_contact_phone")
