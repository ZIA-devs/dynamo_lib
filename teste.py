from dynamo_lib.supabase_bi.crud import BiLogsCRUD
from dynamo_lib.supabase_bi.schemas import BiLogsSchema
from datetime import datetime, timedelta
from pytz import timezone as pytz_timezone


timezone = pytz_timezone("America/Sao_Paulo")


crud = BiLogsCRUD()
start = datetime.now(timezone) - timedelta(days=7)
end = datetime.now(timezone)

print(crud.get_logs(678855738641054, start, end))
