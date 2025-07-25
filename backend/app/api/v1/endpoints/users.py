from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user import create_user, get_user

router = APIRouter()


@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_session)):
    """Create a new user."""
    user_exists = db.query(UserRead).filter(UserRead.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_session)):
    """Retrieve a user by ID."""
    user = get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
