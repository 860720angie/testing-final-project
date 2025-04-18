import pytest
import requests

@pytest.fixture
def base_url():
    return "http://localhost:5000"

def test_homepage_real(base_url):
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200
    assert "Welcome, you are visitor number" in response.text

def test_hello_with_name(base_url):
    response = requests.get(f"{base_url}/hello?name=Anyelo")
    assert response.status_code == 200
    assert "Hello, Anyelo" in response.text

def test_hello_without_name(base_url):
    response = requests.get(f"{base_url}/hello")
    assert response.status_code == 200
    assert "Hello, mysterious visitor" in response.text

def test_hello_form(base_url):
    response = requests.get(f"{base_url}/hello-form")
    assert response.status_code == 200
    assert "<form" in response.text
    assert "Say Hello" in response.text

def test_visits_route(base_url):
    response = requests.get(f"{base_url}/visits")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_visit_by_valid_id(base_url):
    # First get all visits
    visits_response = requests.get(f"{base_url}/visits")
    visits = visits_response.json()

    if visits:
        first_id = visits[0]["id"]
        response = requests.get(f"{base_url}/visit/{first_id}")
        assert response.status_code == 200
        assert f"Visit #{first_id}" in response.text
        assert "IP:" in response.text
        assert "User agent:" in response.text
    else:
        pytest.skip("No visits found to test valid ID.")


def test_visit_by_invalid_id(base_url):
    response = requests.get(f"{base_url}/visit/99999")
    assert response.status_code == 404
    assert "Visit not found" in response.text

