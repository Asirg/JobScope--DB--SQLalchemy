from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

import datetime

from src.annotated import intpk, created_at, updated_at, name255

from src.database import Base


class Sources(Base):
    __tablename__ = 'sources'

    source_id: Mapped[intpk]

    name: Mapped[name255]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]



class RawVacancies(Base):
    __tablename__ = "raw_vacancies"

    raw_vacancy_id:Mapped[intpk]

    source_id:Mapped[int] = mapped_column(ForeignKey("sources.source_id", ondelete="SET NULL"))

    link: Mapped[str]
    name: Mapped[name255]
    data: Mapped[str]
    
    published_at: Mapped[datetime.datetime]
    unpublished_at: Mapped[datetime.datetime]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]