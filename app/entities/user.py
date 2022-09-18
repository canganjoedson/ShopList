from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

#if TYPE_CHECKING:
from .product import Product  # noqa: F401

class User(Base):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, index=True)
    first_name: str = Column(String(50), nullable=False)
    last_name: str = Column(String(50), nullable=False)
    full_name: str = Column(String(250), nullable=False)
    username = Column(String(64), index=True, unique=True)
    email: str = Column(String(150), nullable=False, unique=True)
    image: str = Column(String(250))
    hashed_password: str = Column(String(150), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    joined_at = Column(DateTime())

    products = relationship(Product.__tablename__.title(), back_populates="owner")
