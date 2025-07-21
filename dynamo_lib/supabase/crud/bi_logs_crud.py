from ..core import get_supabase_client
from ..schemas.bi_logs_schema import BiLogsSchema


class BiLogsCRUD:
    def __init__(self, table_name: str):
        self.table_name = table_name
        get_supabase_client().rpc(
            "create_logs_table_if_not_exists", params={"table_name": self.table_name}
        ).execute()

    def insert_log(self, log_data: BiLogsSchema) -> None:
        data = log_data.model_dump(by_alias=True, exclude={"id"})
        get_supabase_client().table(self.table_name).insert(data).execute()

    def get_logs(self, client_id: str) -> list[BiLogsSchema]:
        response = (
            get_supabase_client()
            .table(self.table_name)
            .select("*")
            .eq("client_id", client_id)
            .execute()
        )

        return [BiLogsSchema(**log) for log in response.data]
