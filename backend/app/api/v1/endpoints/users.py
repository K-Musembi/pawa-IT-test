from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services.user import create_user, get_user, update_user as update_user_service

router = APIRouter()


@router.post("/users/", response_model=UserRead, status_code=201)
def create_new_user(user: UserCreate, db: Session = Depends(get_session)):
    """Create a new user."""
    user_exists = db.query(UserRead).filter(UserRead.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    return create_user(db=db, user=user)

@router.post("/users/login", response_model=UserRead, status_code=200)
def login_user(user: UserCreate, db: Session = Depends(get_session)):
    """Login a user."""
    
    user_record = db.query(UserRead).filter(UserRead.username == user.username).first()
    if not user_record or not user_record.verify_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user_record

@router.put("/users/{user_id}", response_model=UserUpdate, status_code=200)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_session)):
    """Update an existing user."""
    
    existing_user = db.query(UserRead).filter(UserRead.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = create_user(db=db, user=user, user_id=user_id)
    return updated_user

@router.get("/users/{user_id}", response_model=UserRead, status_code=200)
def read_user_details(user_id: int, db: Session = Depends(get_session)):
    """Retrieve a user by ID."""
    
    user = get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user
