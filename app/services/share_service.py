from sqlmodel import Session
from app.models.share import Share
from app.repositories.share_repository import ShareRepository
from app.repositories.note_repository import NoteRepository
from app.repositories.label_repository import LabelRepository
from fastapi import HTTPException
from app.models.share import ShareRole


class ShareService:
    def __init__(self, db: Session):
        self.shares = ShareRepository(db)
        self.notes = NoteRepository(db)
        self.labels = LabelRepository(db)

    def share_note(
        self, owner_id: int, note_id: int, target_user_id: int, role: ShareRole
    ) -> Share:
        note = self.notes.get_by_id(note_id)
        if not note or note.owner_id != owner_id:
            raise HTTPException(
                status_code=404, detail="Note does not exist or user not authorized"
            )

        share = self.shares.upsert_note_share(
            note_id,
            target_user_id,
            role.value if hasattr(role, "value") else role,
        )
        return share

    def unshare_note(self, owner_id: int, note_id: int, target_user_id: int) -> None:
        note = self.notes.get_by_id(note_id)
        if not note or note.owner_id != owner_id:
            raise HTTPException(
                status_code=404, detail="Note does not exist or user not authorized"
            )

        self.shares.remove_note_share(note_id, target_user_id)

    def share_label(
        self, owner_id: int, label_id: int, target_user_id: int, role: ShareRole
    ) -> Share:
        label = self.labels.get_by_id(label_id)
        if not label or label.owner_id != owner_id:
            raise HTTPException(
                status_code=404, detail="Label does not exist or user not authorized"
            )

        share = self.shares.upsert_label_share(
            label_id,
            target_user_id,
            role.value if hasattr(role, "value") else role,
        )
        return share

    def unshare_label(self, owner_id: int, label_id: int, target_user_id: int) -> None:
        label = self.labels.get_by_id(label_id)
        if not label or label.owner_id != owner_id:
            raise HTTPException(
                status_code=404, detail="Label does not exist or user not authorized"
            )

        self.shares.remove_label_share(label_id, target_user_id)
