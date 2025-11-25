from fastapi import APIRouter, status
from app.models.label import LabelRead, LabelCreate

from app.core.db import DBSession
from app.services.label_service import LabelService
from app.api.deps import CurrentUser

router = APIRouter(prefix="/labels", tags=["Labels"])


@router.get("/", response_model=list[LabelRead])
def list_labels(db: DBSession, current_user: CurrentUser):
    return LabelService(db).list_labels(current_user.id)


@router.post("/", response_model=LabelRead, status_code=status.HTTP_201_CREATED)
def create_label(payload: LabelCreate, db: DBSession, current_user: CurrentUser):
    return LabelService(db).create_label(current_user.id, payload)


@router.delete("/{label_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_label(label_id: int, db: DBSession, current_user: CurrentUser):
    LabelService(db).delete_label(current_user.id, label_id)
    return None
