from pydantic import BaseModel, Field


class CheckoutSchema(BaseModel):
    id: str = Field(alias="item_id", description="ID of the item")
    name: str = Field(alias="item_name", description="Name of the item")
    price: float = Field(alias="item_price", description="Price of the item")
    description: str = Field(
        default="", alias="item_description", description="Description of the item"
    )
