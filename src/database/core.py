from config.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

async_engine = create_async_engine(url=settings.db_url, echo=False)
async_session: AsyncSession = async_sessionmaker(
    bind=async_engine, autoflush=False, autocommit=False, expire_on_commit=False
)


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
