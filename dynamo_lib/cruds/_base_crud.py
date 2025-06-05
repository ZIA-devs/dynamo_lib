from ..core.dynamo import TableName, dynamo_create, dynamo_query, dynamo_update, dynamo_delete, dynamo_scan, dynamo_delete_starting_with
from typing import TypeVar, Generic, Type, Any, Dict, Optional, ClassVar
from pydantic import BaseModel
from enum import Enum

from time import time
from random import getrandbits
from loguru import logger


T = TypeVar("T", bound=BaseModel)

class BaseCrud(Generic[T]):
    TABLE_NAME: ClassVar[TableName] = 'Companies'
    SK_MARKER: ClassVar[str] = ""
    model: Type[T]
    debug: ClassVar[bool] = False


    @classmethod
    def get_new_id(cls) -> str:
        timestamp_ms = int(time() * 1000)
        random_bits = getrandbits(12)
        return f"{timestamp_ms << 12 | random_bits}"


    @classmethod
    def scan(cls, filter_expression: str | None = None) -> list[T]:
        items = dynamo_scan(table_name=cls.TABLE_NAME, filter_expression=filter_expression)
        if cls.debug: logger.info(f"Scanned items: {items}")
        return [cls.model(**item) for item in items if isinstance(item, dict)]


    @classmethod
    def list(cls, pk: str|int, sk: str|int = '') -> list[T]:
        items = dynamo_query(pk=str(pk), sk=cls.SK_MARKER + str(sk), table_name=cls.TABLE_NAME)
        if cls.debug: logger.info(f"Queried items for pk={pk}, sk={sk}: {items}")
        return [cls.model(**item) for item in items]


    @classmethod
    def get(cls, pk: str|int, sk: str|int = "") -> Optional[T]:
        result = dynamo_query(pk=str(pk), sk=cls.SK_MARKER + str(sk), table_name=cls.TABLE_NAME)
        if cls.debug: logger.info(f"Queried item for pk={pk}, sk={sk}: {result}")
        return cls.model(**result[0]) if result else None


    @classmethod
    def add(cls, pk: str|int, sk: Optional[str|int], data:Dict[str, Any]) -> T:
        sk_text = cls.SK_MARKER + str(sk) if sk is not None else None
        if cls.debug: logger.info(f"Adding item with pk={pk}, sk={sk_text}, data={data}")
        if not dynamo_create(pk=str(pk), sk=sk_text, item=data, table_name=cls.TABLE_NAME):
            raise RuntimeError("Error adding item to DynamoDB")
        return cls.model(**data)
    

    @classmethod
    def add_with_id(cls, pk: str|int, data:Dict[str, Any], id_key:str, sk: str|int="") -> T:
        item_id = cls.get_new_id()
        data[id_key] = item_id
        sk = f'{sk}#{item_id}' if sk else str(item_id)
        if cls.debug: logger.info(f"Adding item with pk={pk}, sk={sk}, data={data}")
        if not dynamo_create(pk=str(pk), sk=cls.SK_MARKER + sk, item=data, table_name=cls.TABLE_NAME):
            raise RuntimeError("Error adding item to DynamoDB")
        return cls.model(**data)


    @classmethod
    def delete_starting_with(cls, pk: str|int, sk: str|int) -> bool:
        if cls.debug: logger.info(f"Deleting all items with pk={pk} starting with sk={cls.SK_MARKER + str(sk)}")
        return dynamo_delete_starting_with(pk, str(sk), cls.TABLE_NAME)
    
    
    @classmethod
    def delete(cls, pk: str|int, sk: str|int = "") -> bool:
        if cls.debug: logger.info(f"Deleting item with pk={pk}, sk={cls.SK_MARKER + str(sk)}")
        return dynamo_delete(pk=str(pk), sk=cls.SK_MARKER + str(sk), table_name=cls.TABLE_NAME)


    @classmethod
    def update(cls, pk: str|int, sk: str|int ="", **kwargs) -> bool:
        allowed_fields = {
            field_name: field.alias
            for field_name, field in cls.model.model_fields.items()
        }
        
        update_values = {}
        for k, v in kwargs.items():
            if k not in allowed_fields: raise ValueError(f"Field '{k}' is not allowed for update.")
            update_values[allowed_fields[k]] = v.value if isinstance(v, Enum) else v
            
        if cls.debug: logger.info(f"Updating item with pk={pk}, sk={cls.SK_MARKER + str(sk)}, update_values={update_values}")
        if not update_values: return False
        return dynamo_update(pk=str(pk), sk=cls.SK_MARKER + str(sk), update_values=update_values, table_name=cls.TABLE_NAME)
