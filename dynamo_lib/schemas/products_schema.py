from pydantic import BaseModel, Field
from typing import List


class ProductsImagesSchema(BaseModel):
    url: str = Field(alias="url")
    description: str = Field(alias="description")


class ProductsSchema(BaseModel):
    id: str = Field(default="", alias="product_id")
    name: str = Field(default="", alias="product_name")
    description: str = Field(default="", alias="product_description")
    price: str = Field(default="", alias="product_price")
    images: List[ProductsImagesSchema] = Field(
        default_factory=List, alias="product_images"
    )
    audios: List[str] = Field(default_factory=List, alias="product_audios")
