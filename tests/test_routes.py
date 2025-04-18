from unittest.mock import patch
from app.main import app
import pytest
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_visit_counter(client):
    fake_visit = {
        "id": 1,
        "ip": "127.0.0.1",
        "timestamp": "2025-04-12T14:00:00",
        "user_agent": "Test-Agent"
    }

    with patch("app.main.add_visit", return_value=fake_visit):
        response = client.get('/')
        assert response.status_code == 200
        assert b"Welcome, you are visitor number" in response.data

def test_visits_route_returns_history(client):
    fake_visits = [
        {
            "id": 1,
            "ip": "127.0.0.1",
            "timestamp": datetime(2024, 1, 1, 10, 0, 0),
            "user_agent": "Test-Agent"
        },
        {
            "id": 2,
            "ip": "192.168.0.1",
            "timestamp": datetime(2025, 4, 12, 15, 0, 0),
            "user_agent": "Another-Agent"
        }
    ]

    with patch("app.main.get_all_visits", return_value=fake_visits):
        response = client.get("/visits")
        assert response.status_code == 200
        assert b"127.0.0.1" in response.data
        assert b"192.168.0.1" in response.data

def test_visit_by_id_returns_details(client):
    fake_visit = {
        "id": 1,
        "ip": "127.0.0.1",
        "timestamp": "2025-04-12T14:00:00",
        "user_agent": "Test-Agent"
    }

    with patch("app.main.get_visit_by_id", return_value=fake_visit):
        response = client.get("/visit/1")
        assert response.status_code == 200
        assert b"127.0.0.1" in response.data
        assert b"Test-Agent" in response.data

def test_hello_with_name(client):
    response = client.get("/hello?name=Anyelo")
    assert response.status_code == 200
    assert b"Hello, Anyelo" in response.data

def test_hello_without_name(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert b"Hello, mysterious visitor" in response.data

def test_hello_form(client):
    response = client.get("/hello-form")
    assert response.status_code == 200
    assert b"<form" in response.data
    assert b"name=" in response.data
    assert b"Say Hello" in response.data

def test_visit_by_id_not_found(client):
    with patch("app.main.get_visit_by_id", return_value=None):
        response = client.get("/visit/9999")
        assert response.status_code == 404
        assert b"Visit not found" in response.data

def test_visits_invalid_from_date(client):
    with patch("app.main.get_all_visits", return_value=[]):
        response = client.get("/visits?from=banana")
        assert response.status_code == 400
        assert b"Invalid" in response.data
        assert b"date format" in response.data

def test_visits_invalid_to_date(client):
    with patch("app.main.get_all_visits", return_value=[]):
        response = client.get("/visits?to=not-a-date")
        assert response.status_code == 400
        assert b"Invalid" in response.data
        assert b"date format" in response.data

def test_visits_valid_from_and_to(client):
    fake_visits = [
        {
            "id": 1,
            "ip": "10.0.0.1",
            "timestamp": datetime(2025, 1, 1, 12, 0),
            "user_agent": "AgentX"
        },
        {
            "id": 2,
            "ip": "10.0.0.2",
            "timestamp": datetime(2025, 1, 15, 14, 0),
            "user_agent": "AgentY"
        }
    ]
    with patch("app.main.get_all_visits", return_value=fake_visits), \
         patch("app.main.format_visit_history", return_value="Visit #1\nVisit #2"):
        response = client.get("/visits?from=2025-01-01&to=2025-01-31")
        assert response.status_code == 200
        assert b"Visit #1" in response.data
        assert b"Visit #2" in response.data

