from typing import Optional
from uuid import UUID

from fastapi import Depends
from fastapi_users import FastAPIUsers, BaseUserManager, UUIDIDMixin
from fastapi_users.authentication import (AuthenticationBackend,
                                          BearerTransport, JWTStrategy)
from fastapi_users.schemas import BaseOAuthAccount
from fastapi_users_db_sqlmodel import SQLModelUserDatabase, SQLModelBaseUserDB
from starlette.requests import Request

from app.core.config import settings
from app.models.user_model import User


class OAuthAccount(BaseOAuthAccount):
    pass


async def get_user_db():
    yield SQLModelBaseUserDB(User, OAuthAccount)


class UserManager(UUIDIDMixin, BaseUserManager[User, UUID]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(
            f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLModelUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY,
                       lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, SQLModelUserDatabase](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
