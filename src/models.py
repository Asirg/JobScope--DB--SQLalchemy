from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, text, String 

from typing import Annotated

import enum
import datetime

from src.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]




class Users(Base):
    __tablename__='users'
    
    user_id: Mapped[intpk]
    username: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class Resumes(Base):
    __tablename__ = "resumes"

    resume_id: Mapped[intpk]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE")) # "SET NULL"

    title: Mapped[str] = mapped_column(String(255))
    active: Mapped[bool] = mapped_column(default=False)
    compensation_min: Mapped[int | None]
    compensation_max: Mapped[int | None]
    Workload: Mapped[Workload]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]















# metadata_obj = MetaData()

# users_table = Table(
#     "users",
#     metadata_obj,
#     Column("user_id", Integer, primary_key=True),
#     Column("username", String),
# )