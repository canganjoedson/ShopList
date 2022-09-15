# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=250))
    category_id = Column(String(length=100))
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="products")
