from pydantic import BaseModel, Field, field_validator
from typing import Dict, List


class CouponSchema(BaseModel):
    code: str = Field(alias="code", description="Cupon code")
    discount: float = Field(alias="discount", description="Discount percentage")


class CheckoutSchema(BaseModel):
    id: str = Field(alias="item_id", description="ID of the item")
    name: str = Field(alias="name", description="Name of the item")
    price: float = Field(alias="price", description="Price of the item")
    description: str = Field(
        default="", alias="description", description="Description of the item"
    )
    coupons: Dict[str, CouponSchema] = Field(
        default=[],
        alias="coupons",
        description="List of coupons associated with the item",
    )

    @field_validator("coupons", mode="before")
    def validate_coupons(cls, value: List | None) -> Dict[str, CouponSchema]:
        if value is None:
            return {}
        if isinstance(value, list):
            return {coupon["code"]: CouponSchema(**coupon) for coupon in value}
        return value
