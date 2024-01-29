from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src import schemas, services
from src.dependencies import get_db

router = APIRouter(
    prefix='/comments',
    tags=['comments']
)


@router.post("/", response_model=schemas.Comment, status_code=201)
async def create_comment(comment: schemas.CommentCreate, db: AsyncSession = Depends(get_db)):
    new_comment = await services.create_comment(database=db, comment=comment)
    try:
        await db.commit()
        return new_comment
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Comment already exists")
