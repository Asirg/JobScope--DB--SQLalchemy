from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, text, String, Index, CheckConstraint

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

    resumes: Mapped[list["Resumes"]] = relationship(
        back_populates="user",
    )

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
    workload: Mapped[Workload]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


    user: Mapped["Users"] = relationship(
        back_populates="resumes",
    )


    __table_args__= (
        Index('title_index', 'title'),
        CheckConstraint("compensation_min > 0", name="check_componsation_positive")
    )