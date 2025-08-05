from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from typing import Optional

import datetime

from src.annotated import intpk, created_at, updated_at, name255

from src.database import Base


class Sources(Base):
    __tablename__ = 'sources'

    source_id: Mapped[intpk]

    name: Mapped[name255]
    link: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]



class RawVacancies(Base):
    __tablename__ = "raw_vacancies"

    raw_vacancy_id:Mapped[intpk]

    source_id:Mapped[int] = mapped_column(ForeignKey("sources.source_id", ondelete="SET NULL"))

    link: Mapped[str]
    name: Mapped[name255]
    data: Mapped[str]
    
    published_at: Mapped[Optional[datetime.datetime]]
    unpublished_at: Mapped[Optional[datetime.datetime]]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

########################################################

class Technologies(Base):
    __tablename__ = "technologies"

    technology_id: Mapped[intpk]
    name: Mapped[name255]

class Specialities(Base):
    __tablename__ = "specialities"

    speciality_id: Mapped[intpk]
    name: Mapped[name255]

class Companies(Base):
    __tablename__ = "companies"

    company_id: Mapped[intpk]
    name: Mapped[name255]
    official_link: Mapped[str]

class Languages(Base):
    __tablename__ = "languages"

    language_id: Mapped[intpk]
    name: Mapped[name255]

class LanguageLevels(Base):
    __tablename__ = "language_levels"

    language_level_id: Mapped[intpk]
    name: Mapped[name255]

########################################################

class Vacancies(Base):
    __tablename__ = "vacancies"

    vacancy_id: Mapped[intpk]

    raw_vacancy_id: Mapped[int] = mapped_column(ForeignKey("raw_vacancies.raw_vacancy_id", ondelete="SET NULL"))

    name: Mapped[name255]
    experience: Mapped[Optional[int]]

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.company_id", ondelete="SET NULL"))
    speciality_id: Mapped[int] = mapped_column(ForeignKey("specialities.speciality_id", ondelete="SET NULL"))


class VacanciesExperienceSpecialities(Base):
    __tablename__ = 'vacancies_experience_specialities'

    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.vacancy_id", ondelete="CASCADE")
        , primary_key=True,
    )

    speciality_id: Mapped[int] = mapped_column(
        ForeignKey("specialities.speciality_id", ondelete="CASCADE")
        , primary_key=True,
    )

class VacanciesTechnologies(Base):
    __tablename__ = 'vacancies_technologies'

    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.vacancy_id", ondelete="CASCADE")
        , primary_key=True
    )

    technology_id: Mapped[int] = mapped_column(
        ForeignKey("technologies.technology_id", ondelete="CASCADE")
        , primary_key=True
    )