from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:qwert54321@localhost:5432/fastapi"

"""
Указание echo=True при инициализации движка позволит нам увидеть сгенерированные SQL-запросы в консоли. 
Мы должны отключить поведение "expire on commit (завершить при фиксации)" для сессий с expire_on_commit=False. 
Это связано с тем, что в настройках async мы не хотим, чтобы SQLAlchemy выдавал новые SQL-запросы к базе данных 
при обращении к уже закоммиченным объектам.
"""
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
Base = declarative_base()
SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

"""
Давайте также определим асинхронную функцию для очистки и воссоздания таблицы базы данных, 
которую мы будем использовать позже
"""


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



