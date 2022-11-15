import pytest

from records.models import Movie, Record


@pytest.fixture(scope='function')
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie
    return _add_movie

@pytest.fixture(scope='function')
def add_record():
    def _add_record(type, is_active,):
        record = Record.objects.create(type=type, is_active=is_active,)
        return record
    return _add_record