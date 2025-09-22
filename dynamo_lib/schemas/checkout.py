from pydantic import BaseModel, Field
from typing import List


class CuponSchema(BaseModel):
    code: str = Field(alias="code", description="Cupon code")
    discount: float = Field(alias="discount", description="Discount percentage")


class CheckoutSchema(BaseModel):
    id: str = Field(alias="item_id", description="ID of the item")
    name: str = Field(alias="name", description="Name of the item")
    price: float = Field(alias="price", description="Price of the item")
    description: str = Field(
        default="", alias="description", description="Description of the item"
    )
    cupons: List[CuponSchema] = Field(
        default=[],
        alias="cupons",
        description="List of cupons associated with the item",
    )
