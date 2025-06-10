from ..schemas import ServiceSchema
from ._base_crud import BaseCrud
from typing import Optional


class ServicesCrud(BaseCrud[ServiceSchema]):
    SK_MARKER = "service#"
    model = ServiceSchema

    @classmethod
    def get_by_name(cls, phone_id: str, name: str) -> Optional[ServiceSchema]:
        services = cls.list(phone_id)
        if not services:
            return None
        for service in services:
            if service.name == name:
                return service
        return None

    @classmethod
    def create(
        cls,
        phone_id: str,
        name: str,
        cost: float,
        duration: int,
        service_id: Optional[int] = None,
    ) -> ServiceSchema:

        service = {
            "service_id": service_id,
            "service_name": name,
            "service_cost": cost,
            "service_duration": duration,
        }
        return cls.add_with_id(pk=phone_id, data=service, id_key="service_id")
