from pydantic import BaseModel, Field


class ProductsOlxSchema(BaseModel):
    id: str = Field(default="", alias="product_olx_id")
    name: str = Field(default="", alias="product_olx_name")
    description: str = Field(default="", alias="product_olx_description")
    price: str = Field(default="", alias="product_olx_price")
    color: str = Field(default="", alias="product_olx_color")
    list_id: str = Field(default="", alias="product_olx_list_id")
