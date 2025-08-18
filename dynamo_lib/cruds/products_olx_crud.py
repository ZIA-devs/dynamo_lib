from ..schemas import ProductsOlxSchema
from ._base_crud import BaseCrud


class ProductsCrud(BaseCrud[ProductsOlxSchema]):
    SK_MARKER = "product_olx#"
    model = ProductsOlxSchema

    @classmethod
    def create(
        cls,
        phone_id: str,
        product_name: str,
        product_price: float,
        product_list_id: str,
        product_description: str = "",
    ) -> ProductsOlxSchema:

        product_dict = {
            "product_olx_name": product_name,
            "product_olx_price": product_price,
            "product_olx_description": product_description,
            "product_olx_list_id": product_list_id,
        }
        return super().add_with_id(
            pk=phone_id, data=product_dict, id_key="product_olx_id"
        )
