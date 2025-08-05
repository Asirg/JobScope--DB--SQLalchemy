from sqlalchemy.orm import Mapped

from src.database import Base

from src.annotated import intpk, created_at, updated_at


class Users(Base):
    __tablename__='users'
    
    user_id: Mapped[intpk]
    username: Mapped[str]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


# class Workload(enum.Enum):
#     parttime = "parttime"
#     fulltime = "fulltime"


# class Resumes(Base):
#     __tablename__ = "resumes"

#     resume_id: Mapped[intpk]

#     user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"))

#     title: Mapped[str] = mapped_column(String(255))
#     active: Mapped[bool] = mapped_column(default=False)
#     compensation_min: Mapped[int | None]
#     compensation_max: Mapped[int | None]
#     workload: Mapped[Workload]

#     created_at: Mapped[created_at]
#     updated_at: Mapped[updated_at]