import typing

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import BaseCategoryRepository
from .models import Base, Category


class CategoryRepository(BaseCategoryRepository):
    def __init__(self, db_path: str):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def count(self) -> int:
        pass

    def find(self, pk: int) -> typing.Optional[Category]:
        pass

    def find_by_name(self, name: str) -> typing.Optional[Category]:
        pass

    def find_all(self) -> typing.List[Category]:
        pass

    def save(self, category: Category) -> bool:
        pass

    def _create(self, *args, **kwargs) -> Category:
        """Helper method for instantiating object from single database row.

        If you want use associative arrays, feel free to modify this function.
        """
        return Category(*args, **kwargs)
