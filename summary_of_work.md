Summary of Work
Built a Flask application with database support (PostgreSQL in production, SQLite for testing).

Used Docker to containerize the app and make it easy to deploy.

Created a comprehensive test plan covering unit, integration, and system testing.

Automated tests with pytest, pytest-cov, and playwright.

Fixed bugs discovered during manual and automated testing.

Achieved over 80% code coverage using mocking for database tests.

How to Run Tests
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt
playwright install

Start the app:
./local-start.sh

Run tests:

Unit + Mock tests:
PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/test_routes.py
PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/test_rendering.py
PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/test_db.py
PYTHONPATH=. pytest tests/test_db_coverage.py --cov=app --cov-report=term-missing


Integration tests: pytest tests/test_integration.py


System test (Playwright): python3 tests/test_system_hello.py

Special Instructions

The app must be running to perform integration/system tests.

Database connections are mocked using unittest.mock to simulate PostgreSQL behavior during unit tests.
