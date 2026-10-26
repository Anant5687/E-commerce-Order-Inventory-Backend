from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users_models import UsersModels
from app.schemas.user_schemas import UserRequest


class UserService:
    @staticmethod
    async def get_all_users(db: AsyncSession):
        result = await db.execute(
            select(UsersModels).where(UsersModels.is_deleted.is_(False))
        )
        users = result.scalars().all()
        return {"status": 200, "message": "Users fetched successfully", "data": users}

    @staticmethod
    async def create_user(
        data: UserRequest,
        db: AsyncSession,
    ) -> UsersModels:

        new_user = UsersModels(**data.model_dump())

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return {"status": 201, "message": "User created successfully", "data": new_user}
