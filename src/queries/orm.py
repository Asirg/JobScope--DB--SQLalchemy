from sqlalchemy import insert, select, update, text, func, cast, Integer, and_
from sqlalchemy.orm import aliased, joinedload, selectinload

from src.database import sync_engine, sync_session, async_session, Base
from models import Users, Resumes, Workload



def create_tables():
    sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True

async def insert_user():
    async with async_session() as session:
        user_asir = Users(username="Asir")
        session.add_all([user_asir])
        await session.commit()

async def select_all_users():
    async with async_session() as session: 
        query = select(Users)
        result = await session.execute(query)
        users = result.scalars().all()
        print(f"{users=}")

async def update_users(user_id: int = 1, new_username:str = "Asirius"):
    async with async_session() as session: 
        user = await session.get(Users, user_id)
        user.username = new_username 
        await session.commit()

async def insert_resumes():
    async with async_session() as session:
        resume_1 = Resumes(
            user_id=1,
            title="Junior Data Engineer",
            active=False,
            compensation_min=500,
            compensation_max=750,
            workload = Workload.fulltime
        )
        resume_2 = Resumes(
            user_id=1,
            title="Junior+ Data Engineer",
            active=False,
            compensation_min=750,
            compensation_max=1000,
            workload = Workload.fulltime
        )
        resume_3 = Resumes(
            user_id=1,
            title="Middle Data Engineer",
            active=False,
            compensation_min=1000,
            compensation_max=1250,
            workload = Workload.fulltime
        )
        resume_4 = Resumes(
            user_id=1,
            title="Middle+ Data Engineer",
            active=True,
            compensation_min=1250,
            compensation_max=1500,
            workload = Workload.fulltime
        )
        session.add_all([resume_1,resume_2,resume_3,resume_4])
        await session.commit()

async def select_resumes_avg_compensation():
    async with async_session() as session:
        query = (
            select(
                Resumes.workload,
                cast(func.avg(Resumes.compensation_min), Integer).label("avg_compensation_min"),
            )
            .select_from(Resumes)
            .where(and_(
                Resumes.title.contains("Data Engineer"),
                Resumes.compensation_min > 0,
            ))
            .group_by(Resumes.workload)
        )
        result = await session.execute(query)
        result = result.all()
        print(result[0].avg_compensation_min)

async def get_avg_diff_compensation():
    async with async_session() as session:
        r = aliased(Resumes)
        u = aliased(Users)
        subq = (
            select(
                r,
                u,
                func.avg(r.compensation_min).over(partition_by=r.workload).cast(Integer).label("avg_workload_compensation")
            )
            .join(r, r.user_id == u.user_id).subquery("helper1")
        )
        cte = (
            select(
                subq.c.user_id,
                subq.c.username,
                subq.c.workload,
                subq.c.compensation_min,
                subq.c.avg_workload_compensation,
                (subq.c.compensation_min - subq.c.avg_workload_compensation).label('compensation_diff'),
            )
            .cte("helper2")
        )
        query = (
            select(cte)
            .order_by(cte.c.compensation_diff.desc())
        )


        result = await session.execute(query)
        result = result.all()
        print(result)



def select_users_with_lazy_relationship():
    with sync_session() as session:
        query = select(Users)
        result = session.execute(query)
        result = result.scalars().all()


        print(result[0].resumes)

def select_users_with_joined_relationship():
    with sync_session() as session:
        query = select(Users).options(joinedload(Users.resumes))
        result = session.execute(query)
        result = result.unique().scalars().all()


        print(result[0].resumes)


def select_users_with_selectin_relationship():
    with sync_session() as session:
        query = select(Users).options(selectinload(Users.resumes))
        result = session.execute(query)
        result = result.unique().scalars().all()


        print(result[0].resumes)





# async def update_users(user_id: int = 1, new_username:str = "Asirius"):
#     async with async_session() as session: 
#         # stmt = text("UPDATE users SET username=:new_username WHERE user_id=:user_id")
#         # stmt = stmt.bindparams(user_id = user_id, new_username = new_username)
#         # stmt = (
#         #     update(Users)
#         #     .values(username=new_username)
#         #     .filter_by(id=user_id)
#         # )
#         user = await session.get(Users, user_id)
#         user.username = new_username 
#         await session.commit()
