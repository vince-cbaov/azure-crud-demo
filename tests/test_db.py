
from unittest.mock import patch
from app import db


@patch('app.db.pyodbc.connect')
def test_get_connection_calls_pyodbc(mock_connect):
    conn = db.get_connection()
    assert mock_connect.called
