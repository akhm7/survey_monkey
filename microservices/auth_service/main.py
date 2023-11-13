from fastapi import FastAPI
from .controllers import router as auth_router

app = FastAPI()

app.include_router(auth_router)
