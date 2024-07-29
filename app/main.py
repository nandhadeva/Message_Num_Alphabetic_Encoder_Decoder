from fastapi import FastAPI
from .routers import decoder


nandha = FastAPI()

nandha.include_router(decoder.router)


@nandha.get('/')
def home():
    return {
        "message": "Hello from main.py"
    }
