from ..schemas import LogsSchema, ConfigsSchema
from .reengagement_crud import ReengagementCrud
from ._base_crud import BaseCrud
from typing import Dict, List
from datetime import datetime, timedelta
from pytz import timezone as pytz_timezone
from json import dumps, loads


timezone = pytz_timezone("America/Sao_Paulo")


class LogsCrud(BaseCrud[LogsSchema]):
    TABLE_NAME = "Logs"
    model = LogsSchema

    def get_msg(
        self, message_type: str, message_body: str, company_config: ConfigsSchema
    ) -> List[str]:

        if message_type == "text":
            return [message_body]

        if message_type == "template" and isinstance(message_body, Dict):
            template_name = message_body.get("name", "")
            match template_name:
                case "lembrete_agendamento":
                    return ["{mensagem de lembrete}"]
                case name if "agendamento" in name:
                    return ["{mensagem do tipo formulario}"]
                case "reengajamento":
                    reengagement = ReengagementCrud.get(company_config.phone_id)
                    if reengagement:
                        return [
                            f"*{company_config.assistant_name}:*\n\n{reengagement.message}"
                        ]
                    return ["{mensagem de reengajamento}"]
                case "cliente_interagiu":
                    return ["{mensagem de aviso de interação}"]
                case _:
                    return ["{mensagem de template}"]

        if message_type in {"interactive", "interactive_list"}:
            return ["{interactive}"]

        if message_type == "contacts":
            message_body = (
                loads(message_body) if isinstance(message_body, str) else message_body
            )
            return [f"{{contacts}}=>{dumps(contact)}" for contact in message_body]

        return [f"{{{message_type}}}=>{message_body}"]

    @classmethod
    def create(
        cls,
        company_config: ConfigsSchema,
        client_phone: str,
        message_body: str,
        message_type: str,
        user_type: int,
    ) -> None:

        msgs = cls().get_msg(message_type, message_body, company_config)
        sender = (
            "user" if user_type == 0 else "assistant" if user_type == 1 else "setor"
        )

        for msg in msgs:
            timestamp = datetime.now(timezone).isoformat()
            data = {
                "client_id": client_phone,
                "message": msg,
                "sender": sender,
                "type": message_type,
                "time": timestamp,
                "ttl": int((datetime.now() + timedelta(days=90)).timestamp()),
            }
            log_sk = f"{client_phone}#{timestamp}"
            super().add(pk=company_config.phone_id, sk=log_sk, data=data)
