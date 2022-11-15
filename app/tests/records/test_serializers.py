from records.serializers import MovieSerializer, RecordSerializer
from rest_framework.exceptions import ErrorDetail

# Movie
def test_valid_movie_serializer():
    valid_serializer_data = {
        "title": "Raising Arizona",
        "genre": "comedy",
        "year": "1987"
    }
    serializer = MovieSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    invalid_serializer_data = {
        "title": "Raising Arizona",
        "genre": "comedy"
    }
    serializer = MovieSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"year": ["This field is required."]}

# Record

def test_valid_record_serializer():
    valid_serializer_data = {
        'is_active': True,
        'type': 'data_point',
        }
    serializer = RecordSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}

def test_invalid_record_serializer():
    invalid_serializer_data = {
        'type': True,
        'is_active': "This is a string not a bool",    
    }
    serializer = RecordSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    print(serializer.errors)
    assert serializer.errors == {'type': \
        [ErrorDetail(string='"True" is not a valid choice.', \
            code='invalid_choice')], \
                'is_active': \
                    [ErrorDetail(string='Must be a valid boolean.', \
                        code='invalid')]}
