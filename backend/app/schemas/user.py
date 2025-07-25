"""User schemas for creating and reading users.""""
from sqlmodel import SQLModel

class UserCreate(SQLModel):
    """UserCreate schema for creating a new user."""
    username: str
    email: str | None = None
    password: str

class UserRead(SQLModel):
    """UserRead schema for reading user information."""
    id: int
    username: str
    email: str

class UserUpdate(SQLModel):
    """UserUpdate schema for updating user information."""
    username: str | None = None
    email: str | None = None
    password: str | None = None
