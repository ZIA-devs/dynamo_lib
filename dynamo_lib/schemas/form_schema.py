from pydantic import BaseModel, Field


class FormSchema(BaseModel):
    logo: str = Field(default="", alias="form_logo")
    min_advance: int = Field(default=30, alias="form_min_advance")
    reminder_time: int = Field(default=1440, alias="form_reminder_time")
    timeout: int = Field(default=1800, alias="form_timeout")
    message: str = Field(default="", alias="form_message")
