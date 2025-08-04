from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine, text

import asyncio

from settings import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,    # Кол-во доступных подключений к бд
    # max_overflow=10 # Кол-во доп подключений к бд
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    # pool_size=5,    # Кол-во доступных подключений к бд
    # max_overflow=10 # Кол-во доп подключений к бд
)


def get_sync_connect():
    with sync_engine.connect() as conn:
        return conn

async def get_async_connect():
    async with async_engine.connect() as conn:
        yield conn

asyncio.run(get_async_connect())