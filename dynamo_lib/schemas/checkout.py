from pydantic import BaseModel, Field
from typing import List


class CuponSchema(BaseModel):
    code: str = Field(alias="cupon_code", description="Cupon code")
    discount: float = Field(alias="cupon_discount", description="Discount percentage")


class CheckoutSchema(BaseModel):
    id: str = Field(alias="item_id", description="ID of the item")
    name: str = Field(alias="item_name", description="Name of the item")
    price: float = Field(alias="item_price", description="Price of the item")
    description: str = Field(
        default="", alias="item_description", description="Description of the item"
    )
    cupons: List[CuponSchema] = Field(
        default=[],
        alias="item_cupons",
        description="List of cupons associated with the item",
    )
