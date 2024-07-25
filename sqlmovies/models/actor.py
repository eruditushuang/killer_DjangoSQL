from sqlalchemy import Column, Integer, String

from .base import Base


class Actor(Base):
    __tablename__ = "actor"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
