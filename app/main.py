from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth import routers

app = FastAPI()

origins = ['http://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

for router, kwargs in routers:
    app.include_router(router=router, **kwargs)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
