from hmac import new
from typing import Any, List

from fastapi import APIRouter, status, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import models
from app.repository import user_repository
from app.schemas import user_schema, token_schema
from app.api import deps
from app.core.config import settings
#from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[user_schema.User])
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    users = user_repository.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/ad", response_model=user_schema.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: user_schema.UserCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user = user_repository.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = user_repository.user.create(db, obj_in=user_in)
    # TODO: Implement email sending 
    # if settings.EMAILS_ENABLED and user_in.email:
    #     send_new_account_email(
    #         email_to=user_in.email, username=user_in.email, password=user_in.password
    #     )
    return user


@router.put("/me", response_model=user_schema.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = user.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = user_repository.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/me", response_model=user_schema.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("", status_code=status.HTTP_201_CREATED, response_model=user_schema.User)
async def create_user(user_in: user_schema.UserCreate, db: Session = Depends(deps.get_db)):
    # TODO: Check if user email doesn't exists
    user_exists = user_repository.user.get_by_email(db, email=user_in.email)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The user with mail already registered")

    new_user = user_repository.user.create(db, obj_in=user_in)

    return user_schema.UserOut(
        id = new_user.id,
        username = new_user.username,
        email = new_user.email,
        first_name = new_user.first_name,
        last_name = new_user.last_name,
        full_name = new_user.full_name,
    )



@router.get("/{user_id}", response_model=user_schema.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = user_repository.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not user_repository.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


@router.put("/{user_id}", response_model=user_schema.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: user_schema.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = user_repository.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = user_repository.user.update(db, db_obj=user, obj_in=user_in)
    return user