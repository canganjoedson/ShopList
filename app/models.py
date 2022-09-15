# coding: utf-8
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(50), nullable=False)
    email: str = Column(String(50), nullable=False)
    hashed_password: str = Column(String(100), nullable=False)

    products = relationship("Product", back_populates="owner")

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), nullable=False)
    description = Column(String(length=250))
    category_id = Column(String(length=100))
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="products")
