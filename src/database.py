from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine, text

import asyncio

from src.settings import settings


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

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_sessionmaker)



class Base(DeclarativeBase):
    pass