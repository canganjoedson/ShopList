from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

#if TYPE_CHECKING:
#from .user import User  # noqa: F401
from .category import Category  # noqa: F401

class Product(Base):
    __tablename__ = 'product'

    id: int = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=250))
    category_id = Column(Integer, ForeignKey("category.id"))
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="products")
    category = relationship(Category.__tablename__.title(), back_populates="products")
