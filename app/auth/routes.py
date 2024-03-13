from fastapi import APIRouter

from .libs import auth_backend, current_active_user, fastapi_users

router = APIRouter()


get_auth_router = fastapi_users.get_auth_router(auth_backend)

routers = [
    (router, dict(prefix="/auth", tags=["auth"])),
    (get_auth_router, dict(prefix="/auth/jwt", tags=["auth"])),
]


