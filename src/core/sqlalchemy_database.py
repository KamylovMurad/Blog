from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from src.core.config import config


class Model(DeclarativeBase):
    pass


async_engine = create_async_engine(
    str(config.POSTGRES_DSN),
    echo=False,
    future=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)
