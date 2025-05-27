from database.core import async_engine, async_session
from sqlalchemy import select

from database.models import Category


async def get_all_categories():
    async with async_session() as session:
        stmt = select(Category)
        categories = await session.execute(stmt)
        return categories.scalars().all()


async def add_new_category(name: str):
    async with async_session() as session:
        category = Category(name=name)
        session.add(category)
        await session.commit()
