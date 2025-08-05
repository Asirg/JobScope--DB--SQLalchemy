from src.database import sync_engine, Base

from src.users.models import *
from src.vacansies.models import *



def create_tables():
    # sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    # sync_engine.echo = True