from sqlalchemy import insert

from src.database import sync_engine, sync_session, async_session, Base
from models import Users



def create_tables():
    # sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    # sync_engine.echo = True

async def insert_data():
    async with async_session() as session:
        user_asir = Users(username="Asir")

        session.add(user_asir)
        await session.commit()