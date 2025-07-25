from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.session import get_session
from app.schemas.user_query import UserQueryRead, UserQueryCreate
from app.services.user_query import create_user_query, get_user_queries
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/user-queries/", response_model=UserQueryRead, status_code=201)
async def create_query_for_user(
    user_query: UserQueryCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Create a new user query for the logged-in user."""
    return await create_user_query(
        db=db, prompt=user_query.prompt, user_id=current_user.id
    )


@router.get("/user-queries/", response_model=list[UserQueryRead], status_code=200)
def read_user_queries(
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Retrieve all queries for the logged-in user."""
    return get_user_queries(db=db, user_id=current_user.id)
