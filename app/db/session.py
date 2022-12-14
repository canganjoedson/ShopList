from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

#engine = create_engine("sqlite:///shoplist.db", connect_args={"check_same_thread": False})
#engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine = create_engine("sqlite:///shoplist.db", pool_pre_ping=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)