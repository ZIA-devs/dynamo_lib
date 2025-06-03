from ..schemas import FaqSchema
from ._base_crud import BaseCrud


class FaqCrud(BaseCrud[FaqSchema]):
    SK_MARKER = "faq#"
    model = FaqSchema

    @classmethod
    def create(cls, phone_id: str, question: str, response:str) -> FaqSchema:
        faq_dict = {
            "faq_question": question,
            "faq_response": response
        }
        return super().add_with_id(pk=phone_id, data=faq_dict, id_key='faq_id')
