from ..core.enums import MessageOrigin
from ..schemas import LogsSchema, ConfigsSchema
from .reengagement_crud import ReengagementCrud
from .client_crud import ClientCrud
from ._base_crud import BaseCrud
from typing import Dict, List
from datetime import datetime, timedelta
import tiktoken
from pytz import timezone as pytz_timezone
from json import dumps, loads

from ..supabase_bi.crud import BiLogsCRUD
from ..supabase_bi.schemas import BiLogsSchema


timezone = pytz_timezone("America/Sao_Paulo")
enc = tiktoken.encoding_for_model("gpt-4o-mini")


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
                case name if "concluir_processo" in name or "agendamento" in name:
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

        elif message_type == "disparo" and isinstance(message_body, Dict):
            template_name = message_body.get("name", "")
            return [f"{{mensagem de disparo}}=>{template_name}"]

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
        message_origin: MessageOrigin = MessageOrigin.META_WPP,
    ) -> None:

        msgs = cls().get_msg(message_type, message_body, company_config)
        sender = (
            "user" if user_type == 0 else "assistant" if user_type == 1 else "setor"
        )

        logs_crud = BiLogsCRUD()

        for msg in msgs:
            timestamp = datetime.now(timezone).isoformat()
            data = {
                "client_id": client_phone,
                "message": msg,
                "sender": sender,
                "type": message_type,
                "time": timestamp,
                "ttl": int((datetime.now() + timedelta(days=90)).timestamp()),
                "message_origin": message_origin,
            }
            log_sk = f"{client_phone}#{timestamp}"
            super().add(pk=company_config.phone_id, sk=log_sk, data=data)
            appointed = False
            canceled = False

            if msg.startswith("{interactive - nfm_reply}"):
                flow_name = msg.split(":")[-1]
                if "cancelar_agendamento" in flow_name:
                    canceled = True
                elif "agendar" in flow_name or "agendamento" in flow_name:
                    appointed = True

            tokens = (
                len(enc.encode(msg)) + (667 if sender == "user" else 0)
                if message_type in {"text", "audio"}
                else 0
            )
            logs_crud.insert_log(
                BiLogsSchema(
                    phone_id=int(company_config.phone_id),
                    client_id=client_phone,
                    sender=sender,
                    appointed=appointed,
                    canceled=canceled,
                    created_at=timestamp,
                    tokens=tokens,
                )
            )

            if sender == "user":
                client = ClientCrud.get(company_config.phone_id, client_phone)

                update = {
                    "msg_count": client.msg_count + 1,
                    "msg_count_wpp": (
                        client.msg_count_wpp + 1
                        if message_origin != MessageOrigin.OLX
                        else client.msg_count_wpp
                    ),
                    "msg_count_olx": (
                        client.msg_count_olx + 1
                        if message_origin == MessageOrigin.OLX
                        else client.msg_count_olx
                    ),
                }
                ClientCrud.update(company_config.phone_id, client_phone, **update)
