import pytest

from records.models import Movie
from records.models import Record


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()
    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title

@pytest.mark.django_db
def test_record_model():
    record = Record(type="Data Point", is_active=True, comment="This is a comment.")
    record.save()
    assert record.type == "Data Point"
    assert record.is_active == True
    assert record.comment == "This is a comment."
    assert type(record.raw_data) == dict
    assert record.created_date
    assert record.updated_date
    assert str(record) == f"{record.type} ID: {record.pk}"