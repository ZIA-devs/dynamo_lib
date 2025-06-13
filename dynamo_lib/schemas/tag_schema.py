from pydantic import BaseModel, Field


class TagSchema(BaseModel):
    id: int = Field(
        alias="tag_id",
        description="ID of the tag",
    )

    name: str = Field(alias="tag_name", description="Name of the tag")

    color: str = Field(
        default="#000000",
        alias="tag_color",
        description="Color of the tag in hex format",
    )
