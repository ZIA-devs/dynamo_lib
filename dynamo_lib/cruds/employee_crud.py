from ..schemas import EmployeeSchema
from ._base_crud import BaseCrud
from typing import Optional, Dict, Any


class EmployeeCrud(BaseCrud[EmployeeSchema]):
    SK_MARKER = "employee#"
    model = EmployeeSchema

    @classmethod
    def get_by_name(cls, phone_id: str, name: str) -> Optional[EmployeeSchema]:
        employees = cls.list(phone_id)
        return next((employee for employee in employees if employee.name == name), None)

    @classmethod
    def create(
        cls,
        phone_id: str,
        name: str,
        employee_id: Optional[int] = None,
        servicos: Optional[list[int]] = None,
        turnos: Optional[Dict[str, bool]] = None,
        shift: Optional[Dict[str, Dict[str, str]]] = None,
    ) -> EmployeeSchema:

        employee: Dict[str, Any] = {"employee_name": name}

        if servicos is not None:
            employee["employee_services"] = servicos

        if turnos is not None:
            employee["morning"] = turnos.get("manha", False)
            employee["afternoon"] = turnos.get("tarde", False)
            employee["night"] = turnos.get("noite", False)

        if shift:
            employee |= shift
        if employee_id is None:
            return super().add_with_id(phone_id, data=employee, id_key="employee_id")
        employee["employee_id"] = employee_id
        return super().add(phone_id, employee_id, employee)
