# Movies Application

## Introduction

This application uses `Python 3`.
You are working on a service for film-lovers.
This service provides its users with the ability to search and manage movie data.

## Task details
Your task is to implement repository pattern with methods that will return valid results about movies to users.
The application uses in-memory `SQLite` database instance that is being wiped before each test.

To complete this task you should:
implement all missing methods in `CategoryRepository` and `MovieReport` classes.
You can use raw SQL or SQLAlchemy ORM - the choice is up to you.

* Please do NOT modify any tests unless specifically told to do so.
* Make tests pass by implementing missing features in the production code.
* There are multiple tests placed in the project that will help verify your solution. 
Please use them as a guide as you develop the project. 
Keep in mind that only a subset of tests is visible to you and that your solution will be tested against many edge cases.

### Task 1 - `sqlmovies/category_repository.py`

Implement missing `CategoryRepository` methods:

 * `count`: return number of categories.
 * `find`: find and return category by id.
 * `find_by_name`: find and return category by name.
 * `find_all`: return all categories.
 * `save`: create or update category record.

### Task 2 - `sqlmovies/movie_report.py`

Implement `MovieReport.get(limit, from_year, to_year, categories)` method:

Returns aggregated data about movies, where every movie is described by fields:

  * `title`
  * `year_of_production`
  * `category_name`
  * `number_of_actors`
  * `actor_names` (concatenated names of movie actors, with default comma separator)

Examples you can find in tests.
Correct ordering: `movie.year_of_production DESC, movie.title ASC`.

## Hints

Think about preventing invalid inputs from being passed to the application (and/or database).

To execute all unit tests, use:

    pip install -q -e . && python3 setup.py pytest
