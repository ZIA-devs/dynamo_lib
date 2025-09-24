from pydantic import BaseModel, Field


class TagSchema(BaseModel):
    id: int = Field(alias="tag_id")
    name: str = Field(alias="tag_name")
    color: str = Field(default="#000000", alias="tag_color")
