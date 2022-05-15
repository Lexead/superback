from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    age: int

    class Config:
        orm_mode = True
