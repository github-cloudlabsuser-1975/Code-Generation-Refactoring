import pytest
from flask import json
from weather_script import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_weather_success(monkeypatch, client):
    class MockResponse:
        status_code = 200
        def json(self):
            return {
                'name': 'Madrid',
                'main': {'temp': 20.5, 'humidity': 60},
                'weather': [{'description': 'cielo claro'}],
                'wind': {'speed': 3.5}
            }
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_get)
    response = client.get('/weather?city=Madrid')
    assert response.status_code == 200
    data = response.get_json()
    assert data['ciudad'] == 'Madrid'
    assert data['temperatura'] == 20.5
    assert data['descripcion'] == 'cielo claro'
    assert data['humedad'] == 60
    assert data['viento'] == 3.5

def test_get_weather_missing_city(client):
    response = client.get('/weather')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Falta el parámetro city'

def test_get_weather_api_error(monkeypatch, client):
    class MockResponse:
        status_code = 404
        def json(self):
            return {}
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr('requests.get', mock_get)
    response = client.get('/weather?city=UnknownCity')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'No se pudo obtener el clima'
