from datetime import datetime
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    description: str | None = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class BookRead(BookBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True