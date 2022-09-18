from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from product import Product  # noqa: F401

class Category(Base):
    __tablename__ = 'category'

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(150), nullable=False)
    image: str = Column(String(250))

    products = relationship("Product", back_populates="category")