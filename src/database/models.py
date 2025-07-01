from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .core import Base
from fastapi_storages.integrations.sqlalchemy import ImageType
from utils.storage import get_storage


class Discount(Base):

    __tablename__ = "discounts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    short_description: Mapped[str] = mapped_column()
    full_description: Mapped[str] = mapped_column()
    promocode: Mapped[str] = mapped_column(nullable=True, default=None)
    validity_period: Mapped[str] = mapped_column()
    partner: Mapped[str] = mapped_column()
    image: Mapped[str] = mapped_column(ImageType(storage=get_storage()))


class User(Base):

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    admin: Mapped[bool] = mapped_column()
