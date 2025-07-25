"""Service for handling user queries in the application."""
from sqlmodel import Session, select
from app.models.user_query import UserQuery
from app.schemas.user_query import UserQueryRead
from app.utils.llm_helper import get_llm_response

async def create_user_query(db: Session, prompt: str, user_id: int) -> UserQuery:
    """Create a new UserQuery instance and add it to the database session."""

    # 1. Get the LLM response asynchronously
    llm_response = await get_llm_response(prompt)

    # 2. Create a new UserQuery instance using prompt and response
    new_query = UserQuery(
        prompt=prompt, response=llm_response, user_id=user_id
    )

    # 3. Add the new query to the database session
    db.add(new_query)
    db.commit()
    db.refresh(new_query)

    # 4. Return the newly created UserQuery instance
    return new_query

def get_user_queries(db: Session, user_id: int) -> list[UserQueryRead]:
    """Retrieve all UserQuery instances for a specific user."""
    return db.query(UserQuery).filter(UserQuery.user_id == user_id).all()
