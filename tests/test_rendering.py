from app.rendering import (
    format_hello_greeting,
    format_visit_details,
    format_visit_history,
    format_welcome_message
)

# Test for /hello?name=
def test_format_hello_with_name():
    result = format_hello_greeting("Anyelo")
    assert "Hello, Anyelo!" in result

def test_format_hello_without_name():
    result = format_hello_greeting("")
    assert "Hello, mysterious visitor!" in result

# Test for /
def test_format_welcome_message():
    result = format_welcome_message({"id": 5})
    assert "visitor number 5" in result
    assert "<html" in result  # basic HTML check

# Test for /visit/<id>
def test_format_visit_details():
    visit = {
        "id": 10,
        "timestamp": "2025-04-12 12:00",
        "ip": "192.168.0.1",
        "user_agent": "Mozilla"
    }
    result = format_visit_details(visit)
    assert "Visit #10" in result
    assert "192.168.0.1" in result
    assert "Mozilla" in result

# Test for /visits
def test_format_visit_history():
    history = [
        {"id": 1, "timestamp": "2025-04-12 10:00"},
        {"id": 2, "timestamp": "2025-04-12 11:00"}
    ]
    result = format_visit_history(history)
    assert "Visit #1" in result
    assert "Visit #2" in result

