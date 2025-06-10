from pydantic import BaseModel, Field
from typing import Dict, Optional, Any, Dict


class CompanyShiftSchema(BaseModel):
    _update_intervals: bool = True

    morning: bool = Field(
        default=False,
        alias=f"morning",
        description="Whether the company has a morning shift",
    )

    start_morning: Dict[str, str] = Field(
        default_factory=dict,
        alias=f"shift_start_morning",
        description="Start time of the morning shift",
    )

    end_morning: Dict[str, str] = Field(
        default_factory=dict,
        alias=f"shift_end_morning",
        description="End time of the morning shift",
    )

    afternoon: bool = Field(
        default=False,
        alias=f"afternoon",
        description="Whether the company has an afternoon shift",
    )

    start_afternoon: dict[str, str] = Field(
        default_factory=dict,
        alias=f"shift_start_afternoon",
        description="Start time of the afternoon shift",
    )

    end_afternoon: dict[str, str] = Field(
        default_factory=dict,
        alias=f"shift_end_afternoon",
        description="End time of the afternoon shift",
    )

    night: bool = Field(
        default=False,
        alias=f"night",
        description="Whether the company has a night shift",
    )

    start_night: dict[str, str] = Field(
        default_factory=dict,
        alias=f"shift_start_night",
        description="Start time of the night shift",
    )

    end_night: dict[str, str] = Field(
        default_factory=dict,
        alias=f"shift_end_night",
        description="End time of the night shift",
    )

    def model_post_init(self, __context: Any) -> None:
        self.process_intervals()

    def clean_none(self, att: dict[str, Any]) -> None:
        keys_to_remove = [key for key, value in att.items() if value is None]
        for key in keys_to_remove:
            del att[key]

    def remove_keys_unique(self, att_1: dict[str, Any], att_2: dict[str, Any]) -> None:
        shared_keys = set(att_1) & set(att_2)
        att_1_keys_to_remove = set(att_1) - shared_keys
        att_2_keys_to_remove = set(att_2) - shared_keys

        for key in att_1_keys_to_remove:
            del att_1[key]
        for key in att_2_keys_to_remove:
            del att_2[key]

    def process_intervals(self) -> None:
        shifts = {
            "morning": (self.start_morning, self.end_morning),
            "afternoon": (self.start_afternoon, self.end_afternoon),
            "night": (self.start_night, self.end_night),
        }

        for shift_name, (start, end) in shifts.items():
            self.clean_none(start)
            self.clean_none(end)
            self.remove_keys_unique(start, end)
            if not self._update_intervals:
                continue
            is_active = bool(start) and bool(end)
            setattr(self, shift_name, is_active)

    def get_turnos(self) -> Dict[str, bool]:
        return {
            "manha": self.morning,
            "tarde": self.afternoon,
            "noite": self.night,
        }

    def format_expediente(self) -> Optional[Dict[str, Dict[str, str]]]:
        expediente_formatado = {}
        turno_times = [
            ("m", self.start_morning, self.end_morning),
            ("t", self.start_afternoon, self.end_afternoon),
            ("n", self.start_night, self.end_night),
        ]

        for i in range(7):
            i_str = str(i)
            turno = {}
            for turno_prefixo, inicio, fim in turno_times:
                if inicio.get(i_str) and fim.get(i_str):
                    turno[f"inicio_{turno_prefixo}"] = inicio[i_str]
                    turno[f"fim_{turno_prefixo}"] = fim[i_str]
            expediente_formatado[i_str] = turno or None

        return expediente_formatado if any(expediente_formatado.values()) else None

    @classmethod
    def recompile_shift(
        cls,
        expediente: Dict[str, Dict[str, str]],
        turnos_base: Dict[str, bool],
        table_var: bool = False,
    ) -> Dict[str, Dict[str, str]]:
        prefix = "shift_" if table_var else ""
        shift_data = {
            f"{prefix}start_morning": {},
            f"{prefix}end_morning": {},
            f"{prefix}start_afternoon": {},
            f"{prefix}end_afternoon": {},
            f"{prefix}start_night": {},
            f"{prefix}end_night": {},
        }

        turnos = []
        if turnos_base.get("manha", False):
            turnos.append(("morning", "inicio_m", "fim_m"))
        if turnos_base.get("tarde", False):
            turnos.append(("afternoon", "inicio_t", "fim_t"))
        if turnos_base.get("noite", False):
            turnos.append(("night", "inicio_n", "fim_n"))

        for k, v in expediente.items():
            if not v:
                continue
            for periodo, inicio_key, fim_key in turnos:
                if not v.get(inicio_key) or not v.get(fim_key):
                    continue
                shift_data[f"{prefix}start_{periodo}"][k] = v.get(inicio_key)
                shift_data[f"{prefix}end_{periodo}"][k] = v.get(fim_key)

        return shift_data
