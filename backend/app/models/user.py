"""User class model with SQLModel ORM."""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    """User class model with SQLModel ORM.
    Represents a user in the system, including their queries.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(unique=True)
    hashed_password: str = Field(nullable=False)

    queries: List["UserQuery"] = Relationship(back_populates="user")
