from app.database.base import BASE
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Boolean, Integer

import uuid


class AddressModel(BASE):
    __tablename__ = "address"

    id: Mapped[str] = mapped_column(default=lambda: str(uuid.uuid4()), primary_key=True)

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), index=True)

    line1: Mapped[str | None] = mapped_column(String(80), nullable=True)

    line2: Mapped[str | None] = mapped_column(String(80), nullable=True)

    city: Mapped[str | None] = mapped_column(String(15))

    state: Mapped[str | None] = mapped_column(String(30))

    postal_code: Mapped[int | None] = mapped_column(Integer(6))

    country: Mapped[str | None] = mapped_column(String(25))

    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
