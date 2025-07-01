from contextlib import asynccontextmanager
import os
import uuid
from fastapi import FastAPI, Request
import uvicorn
from fastapi.staticfiles import StaticFiles

from api_v1.discounts.views import router as discounts_router
from utils.templates import templates
from database.models import Base, Discount
from database.core import async_engine
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from config.config import settings

from database.core import async_engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(discounts_router)
app.mount("/static", StaticFiles(directory="src/static"), name="static")


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        if form['username'] == settings.ADMIN_USERNAME and form['password'] == settings.ADMIN_PASSWORD:
            request.session.update({"token": "..."})
            return True
        else:
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        # Check the token in depth
        return True
    
authentication_backend = AdminAuth(secret_key=settings.ADMIN_SECRETKEY)
admin = Admin(app=app, engine=async_engine, authentication_backend=authentication_backend)

class UserAdmin(ModelView, model=Discount):

    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True
    
    async def save_model(self, request, obj, form, is_created):
        form_data = await request.form()
        print(form)
        uploaded_file = form_data.get("image")
        
        if uploaded_file and uploaded_file.filename:
            # Генерируем уникальное имя
            ext = os.path.splitext(uploaded_file.filename)[1].lower()
            filename = f"{uuid.uuid4().hex}{ext}"
            save_path = os.path.join("static/images", filename)
            
            # Сохраняем файл
            contents = await uploaded_file.read()
            with open(save_path, "wb") as buffer:
                buffer.write(contents)
            
            # Сохраняем ТОЛЬКО имя файла в БД
            obj.image = filename  # Только имя файла!
        
        await super().save_model(request, obj, form, is_created)

admin.add_view(UserAdmin)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host="0.0.0.0")
