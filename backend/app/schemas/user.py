from sqlmodel import SQLMOdel

class UserCreate(SQLMOdel):
    username: str
    email: str
    password: str

class UserRead(SQLMOdel):
    id: int
    username: str
    email: str

class UserUpdate(SQLModel):
    pass
