import boto3
from boto3.dynamodb.conditions import Key

from ._log_wrapper import log_exceptions
from ._table_keys import table_keys

from typing import Any, Optional, Literal, Dict, cast, TYPE_CHECKING
from decimal import Decimal
import os


DEFAULT_TABLE_NAME = 'Companies'
AWS_REGION=os.environ.get('AWS_REGION')
IN_PROD = os.environ.get('IN_PROD') == 'true'
TableName = Literal['Users', 'Control', 'Companies', 'Logs', 'Intents']

_dynamodb = boto3.resource(
    'dynamodb',
    region_name=AWS_REGION
)

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
    dynamodb = cast(DynamoDBServiceResource, _dynamodb)
else:
    dynamodb = _dynamodb


def _get_table_keys(table_name: TableName, pk:Any, sk:Optional[str]) -> Dict[str, Any]:
    table_pk, type_pk = table_keys[table_name]['pk']
    table_sk = table_keys[table_name]['sk']
    if sk is None and table_sk is not None:
        raise ValueError(f"Table {table_name} precisa de uma chave de ordenação (sk).")
    key = {table_pk: type_pk(pk)}
    if sk is not None and table_sk is not None: key[table_sk] = sk
    return key


@log_exceptions
def dynamo_scan(table_name: TableName = DEFAULT_TABLE_NAME, filter_expression: Optional[str] = None) -> list[Dict[str, Any]]:
    table = dynamodb.Table(table_name)
    scan_kwargs = {}
    
    if filter_expression:
        scan_kwargs['FilterExpression'] = filter_expression
    
    response = table.scan(**scan_kwargs)
    return response.get('Items', [])


@log_exceptions
def dynamo_get_gsi(pk_name:str, pk:Any, table_name: TableName, gsi_name: str) -> Optional[Dict[str, Any]]:
    table = dynamodb.Table(table_name)
    response = table.query(
        IndexName=gsi_name,
        KeyConditionExpression=Key(pk_name).eq(pk)
    )
    
    if 'Items' in response and response['Items']:
        return response['Items'][0]
    return None
    
    
@log_exceptions
def dynamo_get(pk: Any, table_name: TableName = DEFAULT_TABLE_NAME, sk: Optional[str] = None) -> Optional[Dict[str, Any]]:
    key = _get_table_keys(table_name, pk, sk)
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    return response.get('Item', None)


@log_exceptions
def dynamo_query(pk: Any, table_name: TableName = DEFAULT_TABLE_NAME, sk: Optional[str] = None) -> list[Dict[str, Any]]:
    table_pk, type_pk = table_keys[table_name]['pk']
    table_sk = table_keys[table_name]['sk']

    key_condition_expression = Key(table_pk).eq(type_pk(pk))
    if sk: key_condition_expression &= Key(table_sk).begins_with(sk)
    table = dynamodb.Table(table_name)
    
    response = table.query(
        KeyConditionExpression=key_condition_expression
    )
    return response.get('Items', [])
    

@log_exceptions
def dynamo_create(pk:Any, item:Dict[str, Any], table_name:TableName = DEFAULT_TABLE_NAME, sk:Optional[str]=None) -> bool:
    key = _get_table_keys(table_name, pk, sk)
    item.update(key)

    for k, v in item.items():
        if isinstance(v, float):
            item[k] = Decimal(str(v))
    
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)
    return True


@log_exceptions
def dynamo_update(pk:Any, update_values:Dict[str, Any], table_name:TableName = DEFAULT_TABLE_NAME, sk:Optional[str]=None) -> bool:
    key = _get_table_keys(table_name, pk, sk)

    for k, v in update_values.items():
        if isinstance(v, float):
            update_values[k] = Decimal(str(v))
    
    update_expr = "SET " + ", ".join([f"#{k}=:{k}" for k in update_values.keys()])
    expr_attr_names = {f"#{k}": k for k in update_values.keys()}
    expr_attr_values = {f":{k}": v for k, v in update_values.items()}

    table = dynamodb.Table(table_name)
    table.update_item(
        Key=key,
        UpdateExpression=update_expr,
        ExpressionAttributeNames=expr_attr_names,
        ExpressionAttributeValues=expr_attr_values
    )
    return True  


@log_exceptions
def dynamo_delete(pk:Any, table_name:TableName = DEFAULT_TABLE_NAME, sk:Optional[str] = None) -> bool:
    key = _get_table_keys(table_name, pk, sk)
    table = dynamodb.Table(table_name)
    table.delete_item(Key=key)
    return True


@log_exceptions
def dynamo_create_from_json(pk: Any, json_object: Dict[str, Any], table_name: TableName = DEFAULT_TABLE_NAME) -> bool:
    for sk, content in json_object.items():
        
        key = _get_table_keys(table_name, pk, sk)
        item = {**key, **content}
        for k, v in item.items():
            if isinstance(v, float):
                item[k] = Decimal(str(v))
        table = dynamodb.Table(table_name)
        table.put_item(Item=item)
    return True
