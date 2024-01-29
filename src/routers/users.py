from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src import schemas, services
from src.dependencies import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post("/", response_model=schemas.User, status_code=201)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = await services.create_user(database=db, user=user)
    try:
        await db.commit()
        return new_user
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="User already exists")


@router.get("/{user_id}/", response_model=schemas.User, status_code=200)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await services.get_user(
        database=db,
        user_id=user_id
    )
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return db_user
