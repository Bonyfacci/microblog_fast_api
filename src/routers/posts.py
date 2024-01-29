from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src import schemas, services
from src.dependencies import get_db

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.post("/", response_model=schemas.Post, status_code=201)
async def create_post(post: schemas.PostCreate, db: AsyncSession = Depends(get_db)):
    new_post = await services.create_post(database=db, post=post)
    try:
        await db.commit()
        return new_post
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Post already exists")


@router.get("/", response_model=list[schemas.Post], status_code=200)
async def read_posts(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    posts = await services.get_posts(
        database=db,
        skip=skip,
        limit=limit
    )
    return posts


@router.get("/{post_id}/", response_model=schemas.Post, status_code=200)
async def read_post(post_id: int, db: AsyncSession = Depends(get_db)):
    db_post = await services.get_post(
        database=db,
        post_id=post_id
    )
    if not db_post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )
    return db_post
