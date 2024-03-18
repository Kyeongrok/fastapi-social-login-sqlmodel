from fastapi import APIRouter

from .libs import auth_backend, fastapi_users
from ..api import report

router = APIRouter()

get_auth_router = fastapi_users.get_auth_router(auth_backend)
# get_verify_router = fastapi_users.get_verify_router()

routers = [
    (router, dict(prefix="/auth", tags=["auth"])),
    (get_auth_router, dict(prefix="/auth/jwt", tags=["auth"])),
    (report.router, dict(prefix="/report", tags=["report"]))
]


