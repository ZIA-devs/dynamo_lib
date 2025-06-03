from ._base_crud import BaseCrud
from core.dynamo import dynamo_get, dynamo_get_gsi
from schemas.user_schema import UserSchema
from core.enums import UserStatus
from typing import Optional


class UsersCrud(BaseCrud[UserSchema]):
    TABLE_NAME = 'Users'
    model = UserSchema

    @classmethod
    def get_user_by_id(cls, user_id: int|str) -> Optional[UserSchema]:
        response = dynamo_get(pk=user_id, table_name=cls.TABLE_NAME)
        return UserSchema(**response) if response else None

    @classmethod
    def get_user_by_email(cls, email: str) -> Optional[UserSchema]:
        response = dynamo_get_gsi(pk_name='email', pk=email, table_name=cls.TABLE_NAME, gsi_name='email')
        if response: return UserSchema(**response)
        else: return None
        
    @classmethod
    def get_user_by_username(cls, username: str) -> Optional[UserSchema]:
        response = dynamo_get_gsi(pk_name='username', pk=username, table_name=cls.TABLE_NAME, gsi_name='username')
        return UserSchema(**response) if response else None

    @classmethod
    def create(cls, company_name:str, name:str, email:str, cnpj:str, username:str, password:str) -> UserSchema:
        user_id = cls.get_new_id()
        user = {
            "cnpj":cnpj,
            "company_id":0,
            "company_name":company_name,
            "email":email,
            "name":name,
            "password":password,
            "status":UserStatus.ACTIVE,
            "username":username
        }
        return super().add(pk=user_id, sk=None, data=user)