from app.database.base import BASE
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, ForeignKey, DateTime
from datetime import datetime

import uuid


class RefreshTokenModels(BASE):
    __tablename__ = "refresh_tokens"

    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4))

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True
    )

    token_hash: Mapped[str] = mapped_column(String(64), unique=True)
    
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    
    revoked_at = Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=True, default=None
    )
