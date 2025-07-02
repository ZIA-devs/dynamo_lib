from ..schemas import ProductsSchema
from ._base_crud import BaseCrud
from typing import Optional, List


class ProductsCrud(BaseCrud[ProductsSchema]):
    SK_MARKER = "product#"
    model = ProductsSchema

    @classmethod
    def create(
        cls,
        phone_id: str,
        product_name: str,
        product_price: float,
        product_description: str = "",
        product_images: Optional[List[str]] = None,
    ) -> ProductsSchema:

        if not product_images:
            product_images = []

        product_dict = {
            "product_name": product_name,
            "product_price": product_price,
            "product_description": product_description,
            "product_images": product_images,
        }
        return super().add_with_id(pk=phone_id, data=product_dict, id_key="product_id")
