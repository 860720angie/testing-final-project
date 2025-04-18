# Flask Visit Counter App 

This is a simple web application built with Flask that tracks website visits and displays visit history, user information, and greeting messages. The project was developed to demonstrate software testing practices using multiple testing strategies.

---

## Features

- Track and store visits with IP and User info
- View visit history and filter by date
- Greet users with custom or anonymous names
- Form to submit your name for a greeting

---

## Tools & Technologies

- **Flask** Web framework
- **PostgreSQL**  for testing Database
- **Docker** Containerization (Dockerfile)
- **Pytest** Unit and integration testing
- **Playwright** System testing (browser automation)

---

## How to Run the Application

### Prerequisites
- Python 3.11
- Docker & Docker Compose
- Virtual Environment (recommended)

### 1. Clone the Repo
```bash
git clone <your-repo-url>
cd testing-final-project
```

### 2. Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Dockerfile from repo
```

### 3. Start the Application
```bash
./local-start.sh
```

The app will be available at:  
`http://localhost:5000` inside Docker VM

---

## How to Run the Tests

### Unit & Mocking Tests (with Pytest)
```bash
# Make sure you're in the project root and virtual environment is active
PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/test_routes.py
PYTHONPATH=. pytest --cov=app --cov-report=term-missing tests/test_rendering.py
PYTHONPATH=. pytest tests/test_db_coverage.py --cov=app --cov-report=term-missing

```

### Integration Tests (requires running app, the application is running locally at http://localhost:5000)
Make sure the app is running before using this:
```bash
pytest tests/test_integration.py

```

### System Test with Playwright
```bash
python3 tests/test_system_hello.py
```

> Note: System test opens the browser. Playwright must be installed and set up.

To install Playwright browsers:
```bash
playwright install
```

---

## Known Issues / Fixes

- **Missing `__init__.py`** in `app/` folder caused test import errors  Fixed by adding the file.
- **Missing `name="name"` attribute** in HTML input caused form submission error Fixed in the HTML.
- **Docker build failed with Python 3.13** due to `greenlet` compatibility issues  
  Fixed by switching the Docker base image to `python:3.11`.  
  Teachers or other users should **not reuse old Dockerfiles with Python 3.13** unless they upgrade dependencies and test thoroughly.

---

## Limitations

- Integration tests require the app to be running.
- Only one Playwright system test implemented.

---

## Authors

**Anyelo**  
**Amine**
**Gabriell**
Testing project for course assignment
