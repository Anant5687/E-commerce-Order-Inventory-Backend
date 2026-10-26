from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.session import create_db
from app.routers.users_routers import router as users_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def health_check():
    return {"status": 200, "details": "Health status 200"}


app.include_router(users_routers)
