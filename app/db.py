
import pyodbc
from contextlib import contextmanager
from app.config import Config

# Connection string for Azure SQL with ODBC Driver 18
_CONN_STR = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={Config.DB_SERVER};"
    f"DATABASE={Config.DB_NAME};"
    f"UID={Config.DB_USER};"
    f"PWD={Config.DB_PASSWORD};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)


def get_connection():
    """Return a live pyodbc connection to Azure SQL.

    Raises pyodbc.Error on connection issues.
    """
    return pyodbc.connect(_CONN_STR)


@contextmanager
def db_cursor():
    """Context manager yielding a cursor with auto-commit/cleanup."""
    conn = get_connection()
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        conn.close()
