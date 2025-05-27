from database.core import async_session
from sqlalchemy import select

from database.models import Discount


async def get_all_discounts():
    async with async_session() as session:
        stmt = select(Discount)
        categories = await session.execute(stmt)
        return categories.scalars().all()


async def get_by_id(p_id: int):
    async with async_session() as session:
        stmt = select(Discount).where(Discount.id == p_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


async def add_new_discount(
    name: str,
    short_description: str,
    full_description: str,
    promocode: str,
    validity_period: str,
    partner: str,
    image: str,
    category: int,
):
    async with async_session() as session:
        discount = Discount(
            name=name,
            short_description=short_description,
            full_description=full_description,
            promocode=promocode,
            validity_period=validity_period,
            partner=partner,
            image=image,
            category_id=category,
        )
        session.add(discount)
        await session.commit()
