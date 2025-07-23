"""UserQuery class model with SQLModel ORM.""""
from SQLModel import SQLMOdel, Field, Relationship
from typing import Optional
from datetime import datetime

class UserQuery(SQLMOdel, table=True):
    """UserQuery class model with SQLModel ORM
    Represents a user's query and response in the system.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    prompt: str = Field(nullable=False)
    response: str = Field(nullable=False)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="queries")
