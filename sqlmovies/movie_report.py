import typing

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
        from_year: typing.Optional[int] = None,
        to_year: typing.Optional[int] = None,
        categories: typing.List[Category] = None,
    ) -> list:
        query = ""
        params = {}

        return self.repository.session.execute(query, params).fetchall()
