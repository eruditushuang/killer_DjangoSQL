import importlib
import json
import os
import unittest

FIXTURES_PATH = "tests/fixtures"


class BaseTestCase(unittest.TestCase):
    repo = None

    def setUp(self):
        self.fixtures = {}
        self.load_fixtures()

    def load_fixtures(self):
        models_module = importlib.import_module("sqlmovies.models")
        for fpath in os.listdir(FIXTURES_PATH):
            with open(os.path.join(FIXTURES_PATH, fpath)) as f:
                objects = json.load(f)

            fname = fpath.split(".")[0]
            self.fixtures[fname] = objects

            for obj in objects:
                if fname == "movie_actor":
                    class_name = fname
                    _cls = getattr(models_module, class_name)
                    self.repo.session.execute(_cls.insert(), obj)
                else:
                    class_name = fname.title()
                    _cls = getattr(models_module, class_name)
                    self.repo.session.add(_cls(**obj))
                    self.repo.session.commit()

    def _convert_to_categories(self, names):
        categories = []
        for cat_name in names:
            categories.append(self.repo.find_by_name(cat_name))
        return categories
