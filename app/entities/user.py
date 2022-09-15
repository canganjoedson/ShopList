from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True)
    first_name: str = Column(String(50), nullable=False)
    last_name: str = Column(String(50), nullable=False)
    full_name: str = Column(String(250), nullable=False)
    email: str = Column(String(50), nullable=False)
    image: str = Column(String(250))
    hashed_password: str = Column(String(100), nullable=False)

    products = relationship("Product", back_populates="owner")
