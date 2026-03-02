
from unittest.mock import patch
from app.crud import create_user, update_user, delete_user, read_users


@patch('app.crud.db_cursor')
def test_create_user(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    result = create_user('Test', 20)
    assert result is True
    ctx.execute.assert_called()


@patch('app.crud.db_cursor')
def test_read_users(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    # Simulate two rows
    ctx.execute.return_value.fetchall.return_value = [
        (1, 'Alice', 29),
        (2, 'Bob', 31),
        (3, 'James', 41),
        (4, 'Jane', 35),
    ]
    users = read_users()
    assert users == [
    {"id": 1, "name": "Alice", "age": 29},
    {"id": 2, "name": "Bob", "age": 31},
    {"id": 3, "name": "James", "age": 41},
    {"id": 4, "name": "Jane", "age": 35},
    ]

@patch('app.crud.db_cursor')
def test_update_user(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    ctx.rowcount = 1
    assert update_user(1, name='New') is True


@patch('app.crud.db_cursor')
def test_delete_user(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    ctx.rowcount = 1
    assert delete_user(1) is True
