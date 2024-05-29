import datetime

from typing import Optional
from pydantic import BaseModel, ConfigDict


class ToDoCreate(BaseModel):
    description: str
    completed: Optional[bool] = False


class ToDoFromDB(ToDoCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime.datetime
