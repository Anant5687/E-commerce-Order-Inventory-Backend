from sqlalchemy.orm import mapped_column, Mapped
from app.database.base import BASE
from app.database.mixins import SoftDeleteMixin
from sqlalchemy import String, Numeric, Boolean, ForeignKey

import uuid


class ProductModels(BASE, SoftDeleteMixin):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()))

    sku: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    name: Mapped[str] = mapped_column(String(60), nullable=False)

    slug: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str | None] = mapped_column(String(100), nullable=True)

    price: Mapped[int] = mapped_column(Numeric(10, 2), nullable=False)

    currency: Mapped[str] = mapped_column(String, nullable=False)

    category_id: Mapped[str | None] = mapped_column(
        ForeignKey("categories.id"), index=True, nullable=False
    )

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
