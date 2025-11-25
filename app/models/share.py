from sqlmodel import Field, SQLModel, UniqueConstraint


class ShareRole(str, Enum):
    READ = "read"
    EDIT = "edit"


class NoteShare(SQLModel, table=True):
    __tablename__ = "note_share"
    __table_args__ = UniqueConstraint(
        "shared_note_id", "shared_with_user_id", name="unique_note_user"
    )

    id: int = Field(default=None, primary_key=True)
    shared_note_id: int = Field(foreign_key="note.id", index=True)
    shared_with_user_id: int = Field(foreign_key="user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


class LabelShare(SQLModel, table=True):
    __tablename__ = "label_share"
    __table_args__ = UniqueConstraint(
        "shared_label_id", "shared_with_user_id", name="unique_label_user"
    )

    id: int = Field(default=None, primary_key=True)
    shared_label_id: int = Field(foreign_key="label.id", index=True)
    shared_with_user_id: int = Field(foreign_key="user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


class ShareRequest(SQLModel):
    target_user_id: int = Field(gt=0)
    role: ShareRole = ShareRole.READ
