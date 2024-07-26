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
        return self.session.query(Category).count()

    def find(self, pk: int) -> typing.Optional[Category]:
        return self.session.query(Category).filter(Category.id == pk).first()  # pk is category id

    def find_by_name(self, name: str) -> typing.Optional[Category]:
        return self.session.query(Category).filter(Category.name == name).first()

    def find_all(self) -> typing.List[Category]:
        return self.session.query(Category).all()

    def save(self, category: Category) -> bool:
        try:
            existing_category = self.find(category.id)
            if existing_category:
                existing_category.name = category.name
            else:
                self.session.add(category)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def _create(self, *args, **kwargs) -> Category:
        """Helper method for instantiating object from single database row.

        If you want use associative arrays, feel free to modify this function.
        """
        return Category(*args, **kwargs)
