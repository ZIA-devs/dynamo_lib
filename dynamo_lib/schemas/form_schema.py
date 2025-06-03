from pydantic import BaseModel, Field


class FormSchema(BaseModel):
    logo: str = Field(default='', alias='form_logo', description='Logo of the company')
    min_advance: int = Field(default=30, alias='form_min_advance', description='Minimum advance time for appointments in minutes')
    reminder_time: int = Field(default=1440, alias='form_reminder_time', description='Reminder time for appointments in minutes')
    timeout: int = Field(default=1800, alias='form_timeout', description='Timeout for appointments in seconds')
