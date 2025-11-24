from sqlmodel import Session
from app.models.label import Label
from app.repositories.label_repository import LabelRepository


class LabelService:
    def __init__(self, db: Session):
        self.repository = LabelRepository(db)

    def list_labels(self, owner_id: int) -> list[Label]:
        return self.repository.list_by_user(owner_id)

    def create_label(self, owner_id: int, payload: LabelCreate) -> Label:
        if self.repository.get_by_name(owner_id, payload.name):
            raise HTTPException(status_code=400, detail="Label name already exists")
            
        return self.repository.create(owner_id, payload)

    def delete_label(self, owner_id: int, label_id: int) -> None:
        label = self.repository.get_by_id(label_id)
        if not label or label.owner_id != owner_id:
            raise HTTPException(
                status_code=404, detail="Label does not exist or user not authorized"
            )
        self.repository.delete(label)
