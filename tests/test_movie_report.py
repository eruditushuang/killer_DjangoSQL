from sqlmovies import CategoryRepository, MovieReport

from .base import BaseTestCase

TEST_DATA = [
    # All movies
    (
        [1, None, None, []],
        (
            {
                "title": "Danny Collins",
                "year_of_production": 2015,
                "category_name": "Comedy",
                "number_of_actors": 2,
                "actor_names": "Al Pacino,Annette Bening",
            },
        ),
    ),
    # All thriller movies
    (
        [1, None, None, ["Thriller"]],
        (
            {
                "title": "The Departed",
                "year_of_production": 2006,
                "category_name": "Thriller",
                "number_of_actors": 3,
                "actor_names": "Matt Damon,Leonardo DiCaprio,Jack Nicholson",
            },
        ),
    ),
    # All comedy moviesfrom_year
    (
        [100, 1990, 2015, ["Comedy"]],
        (
            {
                "title": "Danny Collins",
                "year_of_production": 2015,
                "category_name": "Comedy",
                "number_of_actors": 2,
                "actor_names": "Al Pacino,Annette Bening",
            },
            {
                "title": "Last Vegas",
                "year_of_production": 2013,
                "category_name": "Comedy",
                "number_of_actors": 2,
                "actor_names": "Morgan Freeman,Robert De Niro",
            },
        ),
    ),
    # All movies between 1990 and 2013
    (
        [1, 1990, 2013, []],
        (
            {
                "title": "Last Vegas",
                "year_of_production": 2013,
                "category_name": "Comedy",
                "number_of_actors": 2,
                "actor_names": "Morgan Freeman,Robert De Niro",
            },
        ),
    ),
    # Non-reachable conditions, empty result
    ([5, 1990, 2010, ["Romance"]], ()),
]


class TestMovieReport(BaseTestCase):
    def setUp(self):
        self.repo = CategoryRepository("sqlite:///:memory:")
        super().setUp()

    def tearDown(self):
        """Clean up test database."""

    def test_get(self):
        report = MovieReport(self.repo)

        for i, data in enumerate(TEST_DATA):
            args, expected = data
            with self.subTest(i=i):
                args[-1] = self._convert_to_categories(args[-1])
                result = report.get(*args)
                self.assertEqual(len(result), len(expected))

                for res_movie, exp_movie in zip(result, expected):
                    if not isinstance(res_movie, dict):
                        res_movie = dict(res_movie)
                    self.assertDictEqual(res_movie, exp_movie)
