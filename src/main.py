from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles

from api_v1.discounts.views import router as discounts_router
from api_v1.categories.views import router as categories_router
from utils.templates import templates
from database.models import Base
from database.core import async_engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(discounts_router)
app.include_router(categories_router)
app.mount("/static", StaticFiles(directory="src/static"), name="static")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host='0.0.0.0')
