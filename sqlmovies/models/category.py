from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(32), unique=True, nullable=False)
    movies = relationship("Movie")

    def __init__(self, name, id=None):
        self.name = name
        if id:
            self.id = id
