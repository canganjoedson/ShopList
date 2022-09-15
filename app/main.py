# from unicodedata import name
# from fastapi import FastAPI, HTTPException, Depends, status
# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session, sessionmaker
# from pydantic import BaseModel
# from passlib.context import CryptContext

# from .models import User

# app = FastAPI()
# engine = create_engine("sqlite:///shoplist.db", connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# @app.get("/api/users", tags=["Users"])
# async def get_users(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     return {"users": users}

# @app.post("/api/users", tags=["Users"], status_code=status.HTTP_201_CREATED, response_model=UserModel)
# async def create_user(user_in: UserIn, db: Session = Depends(get_db)):
#     # TODO: Check if user email doesn't exists
#     user_exists = db.query(User).filter(User.email == user_in.email).first()
#     if user_exists:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     hashed_password = get_password_hash(user_in.password)

#     new_user = User(name = user_in.name, email = user_in.email, hashed_password = hashed_password)

#     db.add(new_user)
#     db.commit() 
#     db.refresh(new_user)

#     return UserOut(**new_user)