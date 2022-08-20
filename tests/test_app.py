import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'
