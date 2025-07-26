from sqlmodel import Session
from passlib.context import CryptContext
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hashed_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return pw_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a hashed password against a plain password."""
    return pw_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: UserCreate) -> User:
    """Create a new user in the database."""
    hashed_password = get_hashed_password(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> User | None:
    """Retrieve user details from the database"""
    return db.get(User, user_id)

def update_user(db: Session, user: UserUpdate) -> User:
    """Update user details in the database"""
    pass
