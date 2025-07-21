from dynamo_lib.supabase_bi.crud import BiLogsCRUD
from dynamo_lib.supabase_bi.schemas import BiLogsSchema
from datetime import datetime
from pytz import timezone as pytz_timezone


timezone = pytz_timezone("America/Sao_Paulo")


crud = BiLogsCRUD()
crud.insert_log(
    BiLogsSchema(
        phone_id=12345,
        client_id="5562958429500",
        sender="user",
        appointed=True,
        canceled=False,
        created_at=datetime.now(timezone).isoformat(),
    )
)

print(crud.get_logs(phone_id="12345"))
