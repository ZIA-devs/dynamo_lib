from ..schemas import LogsSchema, ConfigsSchema
from .reengagement_crud import ReengagementCrud
from ._base_crud import BaseCrud
from typing import Dict, Any
from datetime import datetime
import pytz 


timezone = pytz.timezone('America/Sao_Paulo')
class LogsCrud(BaseCrud[LogsSchema]):
    TABLE_NAME = "Logs"
    model = LogsSchema


    def get_msg(self, message_type: str, message_body: str | Dict[str, Any], company_config: ConfigsSchema) -> str:
        if message_type == 'text': return str(message_body)
        if message_type == 'template' and isinstance(message_body, dict):
            template_name = message_body.get('name', '')
            match template_name:
                case 'lembrete_agendamento': return "{mensagem de lembrete}"
                case name if "agendamento" in name:  return "{mensagem do tipo formulario}"
                case 'reengajamento':
                    reengagement = ReengagementCrud.get(company_config.phone_id)
                    if reengagement: return f"*{company_config.assistant_name}:*\n\n{reengagement.message}"
                    return "{mensagem de reengajamento}"
                case 'cliente_interagiu': return "{mensagem de aviso de interação}"
                case _: return "{mensagem de template}"

        if message_type == 'interactive': return "{interactive}"
        return f'{{{message_type}}}=>{message_body}'


    @classmethod
    def create(cls, company_config: ConfigsSchema, client_phone: str, message_body: str | Dict[str, Any], message_type: str, user_type:int) -> LogsSchema:
        msg = cls().get_msg(message_type, message_body, company_config)
        sender = 'user' if user_type == 0 else 'assistant' if user_type == 1 else 'setor'
        timestamp = datetime.now(timezone).isoformat()

        data = {
            'client_id': client_phone,
            'message': msg,
            'sender': sender,
            'type': message_type,
            'time': timestamp
        }  
        log_sk = f"{client_phone}#{timestamp}"
        return super().add(pk=company_config.phone_id, sk=log_sk, data=data)
