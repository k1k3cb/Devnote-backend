from app.core.config import settings
from sqlmodel import create_engine, SQLModel, Session
from typing import Iterator


engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args=(
        {"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else {}
    ),
)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)  # dev
    # SQLModel.metadata.drop_all(engine) #prod


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
