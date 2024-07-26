import typing

from sqlalchemy.orm import Session

from . import Movie
from .base import BaseMovieReport
from .category_repository import CategoryRepository
from .models import Category


class MovieReport(BaseMovieReport):
    """
    Returns aggregated data about movies.
    """

    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def get(
            self,
            limit: int = 3,
            from_year: int = None,
            to_year: int = None,
            categories: list = None,
    ) -> list:

        query = self.repository.session.query(Movie)

        if from_year is not None:
            query = query.filter(Movie.year_of_production >= from_year)
        if to_year is not None:
            query = query.filter(Movie.year_of_production <= to_year)
        if Category is not None:
            query = query.join(Category).filter(Category.id.in_([c.id for c in categories]))
        return query
