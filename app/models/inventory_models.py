from app.database.base import BASE
from app.database.mixins import SoftDeleteMixin, TimestampMixin

import uuid

from sqlalchemy import Column, String

class InventoryModels(BASE, SoftDeleteMixin, TimestampMixin):

    __tablename__ = "inventory"

    id = Column(
        String, primary_key=True, unique=True, default=lambda: str(uuid.uuid4())
    )