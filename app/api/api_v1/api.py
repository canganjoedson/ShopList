from fastapi import APIRouter

from app.api.api_v1.controllers import auth, users

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
#api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
#api_router.include_router(items.router, prefix="/items", tags=["items"])