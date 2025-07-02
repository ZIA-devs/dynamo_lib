from pydantic import BaseModel, Field


class ProductsSchema(BaseModel):
    id: str = Field(
        default="", alias="product_id", description="Unique identifier for the product"
    )

    name: str = Field(
        default="", alias="product_name", description="Name of the product"
    )

    description: str = Field(
        default="",
        alias="product_description",
        description="Description of the product",
    )

    price: str = Field(
        default="", alias="product_price", description="Price of the product"
    )

    images: list[str] = Field(
        default_factory=list,
        alias="product_images",
        description="List of image URLs for the product",
    )
