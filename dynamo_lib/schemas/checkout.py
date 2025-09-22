from pydantic import BaseModel, Field
from typing import Dict


class CheckoutSchema(BaseModel):
    id: str = Field(alias="item_id", description="ID of the item")
    name: str = Field(alias="name", description="Name of the item")
    price: float = Field(alias="price", description="Price of the item")
    description: str = Field(
        default="", alias="description", description="Description of the item"
    )
    coupons: Dict[str, float] = Field(
        default_factory=dict,
        alias="coupons",
        description="List of coupons associated with the item",
    )
