from pydantic import BaseModel, Field
from typing import List


class ProductsImagesSchema(BaseModel):
    url: str = Field(alias="url", description="URL of the product image")
    description: str = Field(
        alias="description",
        description="Description of the product image",
    )


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

    images: List[ProductsImagesSchema] = Field(
        default_factory=List,
        alias="product_images",
        description="List of image URLs for the product",
    )
