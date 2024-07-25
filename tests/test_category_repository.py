import unittest

from sqlmovies import Category, CategoryRepository

from .base import BaseTestCase


class TestCategoryRepositoryEmpty(unittest.TestCase):
    def setUp(self):
        self.repo = CategoryRepository("sqlite:///:memory:")

    def test_find_all(self):
        self.assertEqual(self.repo.find_all(), [])

    def test_non_existing(self):
        pk = -1
        self.assertIsNone(self.repo.find(pk))

    def test_count(self):
        self.assertEqual(self.repo.count(), 0)


class TestCategoryRepository(BaseTestCase):
    def setUp(self):
        self.repo = CategoryRepository("sqlite:///:memory:")
        super().setUp()

    def tearDown(self):
        """Clean up test database."""

    def test_save_new(self):
        category = Category("Western")
        self.assertEqual(category.id, None)
        self.repo.save(category)
        self.assertEqual(category.id, 22)

    def test_save_existing(self):
        category = Category("Action", 1)
        self.assertEqual(category.name, "Action")
        self.repo.save(category)

        category.name = "Action CHANGED"
        self.repo.save(category)

        found_cat = self.repo.find_by_name("Action CHANGED")
        self.assertEqual(found_cat.name, "Action CHANGED")
        self.assertEqual(found_cat.id, category.id)

    def test_count(self):
        dataset = self.fixtures["category"]
        category = self.repo.count()
        self.assertEqual(len(dataset), category)

    def test_find(self):
        dataset = self.fixtures["category"]
        pk = 1
        category = self.repo.find(pk)
        for fixture in dataset:
            if fixture["id"] == pk:
                self.assertIsInstance(category, Category)
                self.assertEqual(fixture["id"], category.id)
                self.assertEqual(fixture["name"], category.name)
                break
        else:
            raise Exception("Invalid test parameter or dataset")

    def test_find_by_name(self):
        dataset = self.fixtures["category"]
        name = "Comedy"
        category = self.repo.find_by_name(name)
        for fixture in dataset:
            if fixture["name"] == name:
                self.assertIsInstance(category, Category)
                self.assertEqual(fixture["id"], category.id)
                self.assertEqual(fixture["name"], category.name)
                break
        else:
            raise Exception("Invalid test parameter or dataset")

    def test_find_all(self):
        dataset = self.fixtures["category"]
        categories = self.repo.find_all()

        for category, fixture in zip(categories, dataset):
            self.assertIsInstance(category, Category)
            self.assertEqual(category.id, fixture["id"])
            self.assertEqual(category.name, fixture["name"])

        self.assertEqual(len(categories), len(dataset))
