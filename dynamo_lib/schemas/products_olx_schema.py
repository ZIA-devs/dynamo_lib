from pydantic import BaseModel, Field


class ProductsOlxSchema(BaseModel):
    id: str = Field(
        default="",
        alias="product_olx_id",
        description="Unique identifier for the product",
    )

    name: str = Field(
        default="", alias="product_olx_name", description="Name of the product"
    )

    description: str = Field(
        default="",
        alias="product_olx_description",
        description="Description of the product",
    )

    price: str = Field(
        default="", alias="product_olx_price", description="Price of the product"
    )

    color: str = Field(
        default="", alias="product_olx_color", description="Color of the product tag"
    )

    list_id: str = Field(
        default="",
        alias="product_olx_list_id",
        description="ID of the list the product belongs to",
    )
