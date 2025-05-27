from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .core import Base


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()


class Discount(Base):

    __tablename__ = "discounts"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    short_description: Mapped[str] = mapped_column()
    full_description: Mapped[str] = mapped_column()
    promocode: Mapped[str] = mapped_column(nullable=True, default=None)
    validity_period: Mapped[str] = mapped_column()
    partner: Mapped[str] = mapped_column()
    image: Mapped[str] = mapped_column()
    category_id: Mapped[str] = mapped_column(ForeignKey("categories.id"))
