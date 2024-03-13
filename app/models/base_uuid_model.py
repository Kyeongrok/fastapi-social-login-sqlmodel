from datetime import datetime
from uuid import UUID

from sqlmodel import SQLModel, Field

from app.utils.uuid6 import uuid7


class BaseUUIDModel(SQLModel):
    id: UUID = Field(default_factory=uuid7, primary_key=True, index=True, nullable=False)
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )
    created_at: datetime | None = Field(default_factory=datetime.utcnow)