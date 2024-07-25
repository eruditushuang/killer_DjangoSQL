import abc
import typing

from .models import Category


class BaseCategoryRepository(abc.ABC):
    """Base CategoryRepository Class."""

    @abc.abstractmethod
    def count(self) -> int:
        pass

    @abc.abstractmethod
    def find(self, pk: int) -> typing.Optional[Category]:
        pass

    @abc.abstractmethod
    def find_by_name(self, name: str) -> typing.Optional[Category]:
        pass

    @abc.abstractmethod
    def find_all(self) -> typing.List[Category]:
        pass

    @abc.abstractmethod
    def save(self, category: Category) -> bool:
        pass


class BaseMovieReport(abc.ABC):
    """Base MovieReport Class."""

    @abc.abstractmethod
    def get(
        self,
        limit: int = 3,
        from_year: typing.Optional[int] = None,
        to_year: typing.Optional[int] = None,
        categories: typing.List[Category] = None,
    ) -> list:
        pass
