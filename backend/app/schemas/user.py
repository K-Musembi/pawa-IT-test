"""User schemas for creating and reading users.""""
from sqlmodel import SQLMOdel

class UserCreate(SQLMOdel):
    """UserCreate schema for creating a new user."""
    username: str
    email: str
    password: str

class UserRead(SQLMOdel):
    """UserRead schema for reading user information."""
    id: int
    username: str
    email: str

class UserUpdate(SQLModel):
    """UserUpdate schema for updating user information."""
    pass
