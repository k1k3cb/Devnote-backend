from fastapi import APIRouter, status
from app.models.user import UserRead, UserCreate
from app.repositories.user_repository import UserRepository
from app.core.db import DBSession
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: DBSession):
    service = AuthService(UserRepository(db))
    return service.register(payload)


@router.post("/login")
def login(email: str, password: str, db: DBSession):
    service = AuthService(UserRepository(db))
    token = service.login(email, password)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token")
def login(db: DBSession, form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    service = AuthService(UserRepository(db))
    token = service.login(email, password)
    return {"access_token": token, "token_type": "bearer"}
