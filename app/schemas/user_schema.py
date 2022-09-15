from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

class UserUpdate(UserBase):
    pass
    
class User(UserBase):
    id: int

    class Config:
        orm_mode = True