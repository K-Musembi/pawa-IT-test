from sqlmodel import SQLMOdel
from datetime import datetime

class UserQueryCreate(SQLMOdel):
    prompt: str
    response: str

class UserQueryRead(SQLModel):
    id: int
    prompt: str
    response: str
    timestamp: datetime
