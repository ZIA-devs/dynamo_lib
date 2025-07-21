import supabase
from ..core import get_supabase_client
from ..schemas.bi_logs_schema import BiLogsSchema

TABLE_NAME = "logs"


class BiLogsCRUD:
    def __init__(self):
        self.client = get_supabase_client()

    def insert_log(self, log_data: BiLogsSchema) -> None:
        data = log_data.model_dump(by_alias=True, exclude={"id"})
        self.client.table(TABLE_NAME).insert(data).execute()

    def get_logs(self, phone_id: str | int) -> list[BiLogsSchema]:
        response = (
            get_supabase_client()
            .table(TABLE_NAME)
            .select("*")
            .eq("phone_id", int(phone_id))
            .execute()
        )

        return [BiLogsSchema(**log) for log in response.data]
