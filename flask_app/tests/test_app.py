import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_flask_hello(client):
    response = client.get("/flask/hello")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello from Flask!"}
