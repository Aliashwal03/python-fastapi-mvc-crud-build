from pydantic import BaseModel
from typing import Optional, List


class CommentSchema(BaseModel):
  id: Optional[int] = True
  content: str

  class Config:
    orm_mode = True