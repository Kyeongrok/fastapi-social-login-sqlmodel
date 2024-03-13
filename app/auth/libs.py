from fastapi_users import fastapi_users, FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend,
                                          BearerTransport, JWTStrategy)
from fastapi_users_db_sqlmodel import SQLModelUserDatabase

from app.core.config import settings
from app.models.user_model import User


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY,
                       lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60)

async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, SQLModelUserDatabase](
    get_user_manager, [auth_backend])


current_active_user = fastapi_users.current_user(active=True)
