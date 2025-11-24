from app.core.security import hash_password
from app.models.user import User, UserCreate
from app.repositories.user_repository import UserRepository
from app.core.security import verify_password, create_access_token
from fastapi import HTTPException


class AuthService:
    def __init__(self, repository: UserRepository):
        self.repository = repository


def register(self, payload: UserCreate) -> User:
    if self.repository.get_by_email(payload.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=hash_password(payload.password[:72]),
    )

    return self.repository.create(user)


def login(self, email: str, password: str) -> dict:
    user = self.repository.get_by_email(email)
    if not user or not verify_password(password[:72], user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)})
    return access_token
