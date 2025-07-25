from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlmodel import Session

from app.core.config import settings
from app.db.session import get_session
from app.models.user import User
from app.schemas.token import TokenPayload
from app.services.user import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def create_access_token(subject: str | Any, expires_delta: timedelta | None = None) -> str:
    """Generates a JWT access token."""
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str, credentials_exception: HTTPException) -> TokenPayload:
    """Verifies the JWT access token and returns its payload."""
    try:
        payload = jwt.decode(token, settings.JWT_KEY, algorithms=[settings.JWT_ALGORITHM])
        return TokenPayload(**payload)
    except JWTError as e:
        raise credentials_exception from e


def get_current_user(db: Session = Depends(get_session), token: str = Depends(oauth2_scheme)) -> User:
    """Dependency to get the current user from a JWT."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_access_token(token, credentials_exception)
    if not token_data.sub:
        raise credentials_exception
    user = get_user(db, user_id=int(token_data.sub))
    if not user:
        raise credentials_exception
    return user
