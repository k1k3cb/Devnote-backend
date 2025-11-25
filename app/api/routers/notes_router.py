from fastapi import APIRouter, status, Depends
from app.models.note import NoteRead, NoteCreate, NoteUpdate
from app.repositories.note_repository import NoteRepository
from app.core.db import DBSession
from app.services.note_service import NoteService
from app.api.deps import CurrentUser

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get("/", response_model=list[NoteRead])
def list_notes(db: DBSession, current_user: CurrentUser):
    return NoteService(db).list_visible_notes(current_user.id)


@router.post("/", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, db: DBSession, current_user: CurrentUser):
    return NoteService(db).create_note(current_user.id, payload)

@router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, payload: NoteUpdate, db: DBSession, current_user: CurrentUser):
    return NoteService(db).update_note(current_user.id, note_id, payload)

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: DBSession, current_user: CurrentUser):
    NoteService(db).delete_note(current_user.id, note_id)
    return None