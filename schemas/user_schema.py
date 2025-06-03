from core.enums import UserStatus
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    user_id: int = Field(default=0, alias='user_id', description='User ID')
    cnpj: str = Field(default='', alias='cnpj', description='CNPJ of the user')
    company_id: int = Field(default=0, alias='company_id', description='Company ID associated with the user')
    company_name: str = Field(default='', alias='company_name', description='Name of the company associated with the user')
    email: str = Field(default='', alias='email', description='Email of the user')
    name: str = Field(default='', alias='name', description='Name of the user')
    password: str = Field(default='', alias='password', description='Password of the user')
    status: UserStatus = Field(default=UserStatus.ACTIVE, alias='status', description='Status of the user')
    username: str = Field(default='', alias='username', description='Username of the user')