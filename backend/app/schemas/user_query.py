"""UserQuery schemas for creating and reading user queries."""
from sqlmodel import SQLModel
from datetime import datetime

class UserQueryCreate(SQLModel):  # Request schema
    """UserQueryCreate schema for creating a new user query."""
    prompt: str

class UserQueryRead(SQLModel):  # Response schema
    """UserQueryRead schema for reading user query information."""
    id: int
    prompt: str
    response: str
    timestamp: datetime
