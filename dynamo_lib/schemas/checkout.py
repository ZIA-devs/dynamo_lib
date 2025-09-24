from pydantic import BaseModel, Field
from typing import Dict


class CheckoutSchema(BaseModel):
    id: str = Field(alias="item_id")
    name: str = Field(alias="name")
    price: float = Field(alias="price")
    description: str = Field(default="", alias="description")
    coupons: Dict[str, float] = Field(default_factory=dict, alias="coupons")
