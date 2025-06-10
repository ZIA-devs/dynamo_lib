from typing import Any, Dict


table_keys: Dict[str, Dict[str, Any]] = {
    "Users": {"pk": ("user_id", int), "sk": None},
    "Control": {"pk": ("company_identification", str), "" "sk": None},
    "Companies": {"pk": ("phone_id", int), "sk": "company_sk"},
    "Logs": {"pk": ("company_id", int), "sk": "logs_sk"},
    "Intents": {"pk": ("plan", int), "sk": "intent"},
}
