import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")


def get_supabase_client() -> Client:
    return create_client(url, key)


def fetch_data(table_name: str, filters: dict = None) -> list:
    client = get_supabase_client()
    response = client.table(table_name).select("*").filter(filters).execute()
    return response.data


def insert_data(table_name: str, data: dict) -> dict:
    client = get_supabase_client()
    response = client.table(table_name).insert(data).execute()
    return response.data


def update_data(table_name: str, data: dict, filters: dict) -> dict:
    client = get_supabase_client()
    response = client.table(table_name).update(data).filter(filters).execute()
    return response.data


def delete_data(table_name: str, filters: dict) -> dict:
    client = get_supabase_client()
    response = client.table(table_name).delete().filter(filters).execute()
    return response.data
