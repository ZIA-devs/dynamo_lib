from dynamo_lib.supabase_bi.crud import BiLogsCRUD
from dynamo_lib.supabase_bi.schemas import BiLogsSchema
from datetime import datetime, timedelta
from pytz import timezone as pytz_timezone


timezone = pytz_timezone("America/Sao_Paulo")


crud = BiLogsCRUD()
start = datetime.strptime("2025-07-01", "%Y-%m-%d")
end = datetime.strptime("2025-07-22", "%Y-%m-%d")

print(crud.get_logs(679117678621080, start, end))
