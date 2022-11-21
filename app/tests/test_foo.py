import json

from django.urls import reverse


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


# client is a pytest-django helper fixture that provides
# an instance of django.test.Client.
def test_ping(client):
    # Given
    # client

    # When
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)

    # Then
    assert response.status_code == 200
    assert content["ping"] == "pong!"
