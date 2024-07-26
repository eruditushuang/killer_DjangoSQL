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
        query = """
        SELECT
            movie.title,
            movie.year_of_production,
            category.name AS category_name,
            COUNT(actor.id) AS number_of_actors,
            GROUP_CONCAT(actor.name, ', ') AS actor_names
        FROM
            movies movie
        JOIN
            categories category ON movie.category_id = category.id
        LEFT JOIN
            movie_actors movie_actor ON movie.id = movie_actor.movie_id
        LEFT JOIN
            actors actor ON movie_actor.actor_id = actor.id
        WHERE
            (? IS NULL OR movie.year_of_production >= :from_year) AND
            (? IS NULL OR movie.year_of_production <= :to_year) AND
            (? IS NULL OR category.id IN :categories)
        GROUP BY
            movie.id
        ORDER BY
            movie.year_of_production DESC,
            movie.title ASC
        LIMIT ?
        """

        params = (from_year, to_year, tuple(category.id for category in categories) if categories else None, limit)

        return self.repository.session.execute(query, params).fetchall()
