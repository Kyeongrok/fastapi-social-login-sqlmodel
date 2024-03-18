from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth import routers
from app.core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

for router, kwargs in routers:
    app.include_router(router=router, **kwargs)


@app.on_event("startup")
async def startup():
    print('APP_ENV:', settings.APP_ENV)
