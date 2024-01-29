from sqlalchemy import select, orm
from sqlalchemy.ext.asyncio import AsyncSession
from src import models, schemas

"""
В get_biggest_cities для создания запроса используется новая функция select. 
Запрос выглядит так же, как если бы он выполнялся непосредственно на объекте сессии. 
Но теперь, вместо вызова session().query(), мы ожидаем session.execute(), 
который выполнит запрос и сохранит результаты. Метод scalars() обеспечивает доступ к результатам.
Функция add_city просто помещает новый объект City в сессию — мы будем управлять транзакцией в контроллере 
(маршрут).
"""


async def get_user(database: AsyncSession, user_id: int):
    res = await database.execute(
        select(models.User).options(orm.joinedload(models.User.all_posts)).where(models.User.id == user_id)
    )
    return res.scalars().first()


async def create_user(database: AsyncSession, user: schemas.UserCreate):
    fake_hashed_password = "<PASSWORD>" + user.password
    db_user = models.User(
        email=user.email,
        password=fake_hashed_password
    )

    database.add(db_user)

    return db_user


async def get_post(database: AsyncSession, post_id: int):
    res = await database.execute(
        select(models.Post).options(orm.joinedload(models.Post.all_comments)).where(models.Post.id == post_id))
    return res.scalars().first()


async def get_posts(database: AsyncSession):
    res = await database.execute(
        select(models.Post))
    return res.scalars().all()


async def create_post(database: AsyncSession, post: schemas.PostCreate):
    db_post = models.Post(
        text=post.text,
        owner_id=post.owner_id,
    )

    database.add(db_post)

    return db_post


async def get_comment(database: AsyncSession, comment_id: int):
    res = await database.execute(
        select(models.Comment).where(models.Comment.id == comment_id))
    return res.scalars().first()


async def create_comment(database: AsyncSession, comment: schemas.CommentCreate):
    db_comment = models.Post(
        owner_id=comment.owner_id,
        text=comment.text,
        post_id=comment.post_id,
    )

    database.add(db_comment)

    return db_comment
