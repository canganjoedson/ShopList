from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str


class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    full_name: str
    image: str | None = None
    
class UserUpdate(UserBase):
    image: str | None = None

class UserCreate(UserBase):
    ''' This model is used to create a new user '''
    password: str
    image: str | None = None

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    full_name: str

    class Config:
        orm_mode = True