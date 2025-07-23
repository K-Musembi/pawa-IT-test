"""UserQuery schemas for creating and reading user queries."""
from sqlmodel import SQLMOdel
from datetime import datetime

class UserQueryCreate(SQLMOdel):
    """UserQueryCreate schema for creating a new user query."""
    prompt: str
    response: str

class UserQueryRead(SQLModel):
    """UserQueryRead schema for reading user query information."""
    id: int
    prompt: str
    response: str
    timestamp: datetime
