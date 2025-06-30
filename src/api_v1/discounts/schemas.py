from typing import Optional
from fastapi import File, UploadFile
from pydantic import BaseModel


class DiscountSchema(BaseModel):
    name: str
    short_description: str
    full_description: str
    promocode: Optional[str] = None
    validity_period: str
    partner: str


class DiscountSchemaImage(DiscountSchema):
    image: str = None
