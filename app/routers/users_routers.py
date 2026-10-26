from app.services.users_services import UserService
from app.schemas.user_schemas import UserRequest, UserResponse, UserResponseAll
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/all", response_model=UserResponseAll)
async def get_all_users(db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.get_all_users(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    except HTTPException as e:
        raise e


@router.post("/create", status_code=201, response_model=UserResponse)
async def create_user(data: UserRequest, db: AsyncSession = Depends(get_db)):
    try:
        return await UserService.create_user(data, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    except HTTPException as e:
        raise e
