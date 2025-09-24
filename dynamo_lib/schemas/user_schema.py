from ..core.enums import UserStatus, UserPermissions
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    user_id: int = Field(default=0, alias="user_id")
    cnpj: str = Field(default="", alias="cnpj")
    company_id: int = Field(default=0, alias="company_id")
    company_name: str = Field(default="", alias="company_name")
    email: str = Field(default="", alias="email")
    name: str = Field(default="", alias="name")
    password: str = Field(default="", alias="password")
    status: UserStatus = Field(default=UserStatus.ACTIVE, alias="status")
    username: str = Field(default="", alias="username")
    permissions: UserPermissions = Field(
        default=UserPermissions.EMPLOYEE, alias="permissions"
    )
