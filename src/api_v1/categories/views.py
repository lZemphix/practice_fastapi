from fastapi import APIRouter, Request
from api_v1.categories.crud import get_all_categories, add_new_category
from utils.templates import templates

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="discounts.html")


@router.get("/get")
async def get():
    return await get_all_categories()


@router.post("/add")
async def add(name: str):
    await add_new_category(name)
    return {"status": "ok"}
