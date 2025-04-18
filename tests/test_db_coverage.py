# tests/test_db_coverage.py
from unittest.mock import patch, MagicMock
from app.db import add_visit, get_all_visits, get_visit_by_id
from datetime import datetime, timezone

@patch("app.db.get_db_connection")
def test_add_visit(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = [1]
    mock_conn_func.return_value = mock_conn

    result = add_visit("127.0.0.1", "Test-Agent")
    assert result["id"] == 1
    assert result["ip"] == "127.0.0.1"

@patch("app.db.get_db_connection")
def test_get_all_visits(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, datetime.now(timezone.utc), "ip", "agent")]
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_all_visits()
    assert len(result) == 1

@patch("app.db.get_db_connection")
def test_get_visit_by_id_found(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1, datetime.now(timezone.utc), "ip", "agent")
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_visit_by_id(1)
    assert result["id"] == 1

@patch("app.db.get_db_connection")
def test_get_visit_by_id_not_found(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_visit_by_id(999)
    assert result is None
# tests/test_db_coverage.py
from unittest.mock import patch, MagicMock
from app.db import add_visit, get_all_visits, get_visit_by_id
from datetime import datetime, timezone

@patch("app.db.get_db_connection")
def test_add_visit(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = [1]
    mock_conn_func.return_value = mock_conn

    result = add_visit("127.0.0.1", "Test-Agent")
    assert result["id"] == 1
    assert result["ip"] == "127.0.0.1"

@patch("app.db.get_db_connection")
def test_get_all_visits(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, datetime.now(timezone.utc), "ip", "agent")]
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_all_visits()
    assert len(result) == 1

@patch("app.db.get_db_connection")
def test_get_visit_by_id_found(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1, datetime.now(timezone.utc), "ip", "agent")
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_visit_by_id(1)
    assert result["id"] == 1

@patch("app.db.get_db_connection")
def test_get_visit_by_id_not_found(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_visit_by_id(999)
    assert result is None
# tests/test_db_coverage.py
from unittest.mock import patch, MagicMock
from app.db import add_visit, get_all_visits, get_visit_by_id
from datetime import datetime, timezone

@patch("app.db.get_db_connection")
def test_add_visit(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = [1]
    mock_conn_func.return_value = mock_conn

    result = add_visit("127.0.0.1", "Test-Agent")
    assert result["id"] == 1
    assert result["ip"] == "127.0.0.1"

@patch("app.db.get_db_connection")
def test_get_all_visits(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [(1, datetime.now(timezone.utc), "ip", "agent")]
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_all_visits()
    assert len(result) == 1

@patch("app.db.get_db_connection")
def test_get_visit_by_id_found(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1, datetime.now(timezone.utc), "ip", "agent")
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_visit_by_id(1)
    assert result["id"] == 1

@patch("app.db.get_db_connection")
def test_get_visit_by_id_not_found(mock_conn_func):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_conn.cursor.return_value = mock_cursor
    mock_conn_func.return_value = mock_conn

    result = get_visit_by_id(999)
    assert result is None

