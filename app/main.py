from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    swagger_ui_parameters={"persistAuthorization": True},
    version="1.0.0",
    description="API para la gestión de notas de desarrollo",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"msg": "hola!"}
