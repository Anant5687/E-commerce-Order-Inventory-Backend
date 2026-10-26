from app.database.base import BASE
from app.database.mixins import SoftDeleteMixin, TimestampMixin

import uuid

from sqlalchemy import Column, String


class UsersModels(BASE, SoftDeleteMixin, TimestampMixin):

    __tablename__ = "users"

    id = Column(String, primary_key=True, unique=True, default=lambda: uuid.uuid4())

    name = Column(String, nullable=False, unique=True)

    email = Column(String, nullable=False)

    password = Column(String, nullable=False)

    phone = Column(String, nullable=False, unique=True)
