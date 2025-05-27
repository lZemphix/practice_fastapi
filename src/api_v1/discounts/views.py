import os
import uuid
from fastapi import APIRouter, Depends, Request, UploadFile, File

from api_v1.discounts.schemas import DiscountSchema
from utils.templates import templates
from api_v1.discounts.crud import *

router = APIRouter(prefix="/discounts", tags=["Discounts"])


@router.get("/")
async def index(request: Request):
    discounts = await get_all_discounts()
    context = {"discounts": discounts}
    return templates.TemplateResponse(
        request=request, name="discounts.html", context=context
    )


@router.get("/{id}")
async def descr(request: Request, id: int):
    discounts = await get_all_discounts()
    discount = await get_by_id(id)
    context = {"description": discount, "discounts": discounts}
    return templates.TemplateResponse(
        request=request, name="description.html", context=context
    )


@router.post("/")
async def add(discount: DiscountSchema = Depends(), image: UploadFile = File(...)):
    filename = f"{uuid.uuid4()}.{image.filename.split('.')[-1]}"
    static_dir = os.path.join(os.path.dirname(__file__), "..", "..", "static", "images")
    file_path = os.path.join(static_dir, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await image.read())

    data = discount.model_dump()

    await add_new_discount(**data, image=f"{filename}")
    return {"status": "success"}
