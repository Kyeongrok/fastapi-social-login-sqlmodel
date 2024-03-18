from fastapi_users import schemas

from fastapi_users_db_sqlmodel import SQLModelUserDatabase, SQLModelBaseUserDB


class UserRead(schemas.BaseUser[SQLModelUserDatabase]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
