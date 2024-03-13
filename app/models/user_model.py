from sqlmodel import SQLModel

from app.models.base_uuid_model import BaseUUIDModel


class UserBase(SQLModel):
    display_name: str
    id_company: str
    user_id: str
    email: str


class User(BaseUUIDModel, UserBase, table=True):
    __tablename__ = "users"
