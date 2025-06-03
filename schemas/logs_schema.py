from pydantic import BaseModel, Field


class LogsSchema(BaseModel):
    company_id: int = Field(default=0, alias='log_company_id', description='ID of the company')
    logs_sk: str = Field(default='', alias='log_sk', description='Unique identifier for the log entry')
    client_id: str = Field(default='', alias='log_client_id', description='ID of the client')
    message: str = Field(default='', alias='log_message', description='Message in the log entry')
    sender: str = Field(default='', alias='log_sender', description='Sender of the message in the log entry')
    type: str = Field(default='', alias='log_type', description='Type of the message in the log entry')
    time: str = Field(default='', alias='log_time', description='Timestamp of the log entry')