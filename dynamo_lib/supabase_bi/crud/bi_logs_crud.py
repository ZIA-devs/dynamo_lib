import supabase
from ..core import get_supabase_client
from ..schemas.bi_logs_schema import BiLogsSchema, BiLogsOutputSchema
from datetime import datetime
from typing import List

TABLE_NAME = "logs"


class BiLogsCRUD:
    def __init__(self):
        self.client = get_supabase_client()

    def insert_log(self, log_data: BiLogsSchema) -> None:
        data = log_data.model_dump(by_alias=True, exclude={"id"})
        self.client.table(TABLE_NAME).insert(data).execute()

    def get_logs(
        self, phone_id: str | int, start: datetime, end: datetime
    ) -> List[BiLogsOutputSchema]:

        response = self.client.rpc(
            "get_logs_summary_by_interval",
            {
                "phone_id": phone_id,
                "date_start": start.isoformat(),
                "date_end": end.isoformat(),
            },
        ).execute()

        return [BiLogsOutputSchema(**log) for log in response.data]
