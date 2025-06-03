from core.dynamo import TableName, dynamo_create, dynamo_query, dynamo_update, dynamo_delete, dynamo_scan
from typing import TypeVar, Generic, Type, Any, Dict, Optional, ClassVar
from pydantic import BaseModel
from enum import Enum

import time
import random

T = TypeVar("T", bound=BaseModel)

class BaseCrud(Generic[T]):
    TABLE_NAME: ClassVar[TableName] = 'Companies'
    SK_MARKER: ClassVar[str] = ""
    model: Type[T]


    @classmethod
    def get_new_id(cls) -> str:
        timestamp_ms = int(time.time() * 1000)
        random_bits = random.getrandbits(12)
        return f"{timestamp_ms << 12 | random_bits}"


    @classmethod
    def scan(cls, filter_expression: str | None = None) -> list[T]:
        items = dynamo_scan(table_name=cls.TABLE_NAME, filter_expression=filter_expression)
        return [cls.model(**item) for item in items if isinstance(item, dict)]


    @classmethod
    def list(cls, pk: str|int, sk: str|int = '') -> list[T]:
        items = dynamo_query(pk=str(pk), sk=cls.SK_MARKER + str(sk), table_name=cls.TABLE_NAME)
        return [cls.model(**item) for item in items]


    @classmethod
    def get(cls, pk: str|int, sk: str|int = "") -> Optional[T]:
        result = dynamo_query(pk=str(pk), sk=cls.SK_MARKER + str(sk), table_name=cls.TABLE_NAME)
        return cls.model(**result[0]) if result else None


    @classmethod
    def add(cls, pk: str|int, sk: Optional[str|int], data:Dict[str, Any]) -> T:
        sk_text = cls.SK_MARKER + str(sk) if sk is not None else None
        if not dynamo_create(pk=str(pk), sk=sk_text, item=data, table_name=cls.TABLE_NAME):
            raise Exception("Error adding item to DynamoDB")
        return cls.model(**data)
    

    @classmethod
    def add_with_id(cls, pk: str|int, data:Dict[str, Any], id_key:str, sk: str|int="") -> T:
        item_id = cls.get_new_id()
        data[id_key] = item_id
        sk = f'{sk}#{item_id}' if sk else str(item_id)
        if not dynamo_create(pk=str(pk), sk=cls.SK_MARKER + sk, item=data, table_name=cls.TABLE_NAME):
            raise Exception("Error adding item to DynamoDB")
        return cls.model(**data)


    @classmethod
    def delete(cls, pk: str|int, sk: str|int = "") -> bool:
        return dynamo_delete(pk=str(pk), sk=cls.SK_MARKER + str(sk), table_name=cls.TABLE_NAME)


    @classmethod
    def update(cls, pk: str|int, sk: str|int ="", **kwargs) -> bool:
        print(kwargs)
        allowed_fields = {
            field_name: field.alias
            for field_name, field in cls.model.model_fields.items()
        }
        
        update_values = {}
        for k, v in kwargs.items():
            if k not in allowed_fields: raise ValueError(f"Field '{k}' is not allowed for update.")
            update_values[allowed_fields[k]] = v.value if isinstance(v, Enum) else v

        if not update_values: return False
        return dynamo_update(pk=str(pk), sk=cls.SK_MARKER + str(sk), update_values=update_values, table_name=cls.TABLE_NAME)
