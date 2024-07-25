from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


movie_actor = Table(
    "movie_actor",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movie.id")),
    Column("actor_id", Integer, ForeignKey("actor.id")),
)


class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    category = relationship("Category", back_populates="movies")
    title = Column(String(32), nullable=False)
    year_of_production = Column(Integer, nullable=False)
    actors = relationship("Movie", secondary=movie_actor, backref="movies")
