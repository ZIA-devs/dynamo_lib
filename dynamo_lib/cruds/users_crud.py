from ..core.dynamo import dynamo_get, dynamo_get_gsi, dynamo_get_gsi_list
from ..schemas.user_schema import UserSchema
from ..core.enums import UserStatus, UserPermissions
from ._base_crud import BaseCrud
from typing import Optional


class UsersCrud(BaseCrud[UserSchema]):
    TABLE_NAME = "Users"
    model = UserSchema

    @classmethod
    def list_users_by_company_name(cls, company_name: str) -> list[UserSchema]:
        response = dynamo_get_gsi_list(
            pk_name="company_name",
            pk=company_name,
            table_name=cls.TABLE_NAME,
            gsi_name="company_name",
        )
        return [UserSchema(**item) for item in response] if response else []

    @classmethod
    def get_user_by_id(cls, user_id: int | str) -> Optional[UserSchema]:
        response = dynamo_get(pk=user_id, table_name=cls.TABLE_NAME)
        return UserSchema(**response) if response else None

    @classmethod
    def get_user_by_email(cls, email: str) -> Optional[UserSchema]:
        response = dynamo_get_gsi(
            pk_name="email", pk=email, table_name=cls.TABLE_NAME, gsi_name="email"
        )
        return UserSchema(**response) if response else None

    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[UserSchema]:
        response = dynamo_get_gsi(
            pk_name="username",
            pk=username,
            table_name=cls.TABLE_NAME,
            gsi_name="username",
        )
        return UserSchema(**response) if response else None

    @classmethod
    def create(
        cls,
        company_name: str,
        name: str,
        email: str,
        cnpj: str,
        username: str,
        password: str,
        permissions: UserPermissions = UserPermissions.EMPLOYEE,
        company_id: int = 0,
    ) -> UserSchema:

        user_id = cls.get_new_id()
        user = {
            "cnpj": cnpj,
            "company_id": company_id,
            "company_name": company_name,
            "email": email,
            "name": name,
            "password": password,
            "status": UserStatus.ACTIVE,
            "username": username,
            "permissions": permissions.value,
        }
        return super().add(pk=user_id, sk=None, data=user)
