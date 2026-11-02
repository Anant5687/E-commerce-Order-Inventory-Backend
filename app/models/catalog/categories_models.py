from app.database.base import BASE
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from app.database.mixins import SoftDeleteMixin

import uuid


class CategoriesModel(BASE, SoftDeleteMixin):
    __tablename__ = "categories"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))

    name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)

    slug: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)

    parent_id: Mapped[str] = mapped_column(ForeignKey("categories.id"), nullable=True)
