"""Database session management for SQLModel with FastAPI."""
from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings


engine = create_engine(settings.DB_URL, echo=True)

def create_db_and_tables():
    """Create the database and tables if they do not exist."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Session:
    """Get a new SQLModel session."""
    with Session(engine) as session:
        yield session