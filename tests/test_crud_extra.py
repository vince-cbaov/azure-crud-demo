# tests/test_crud_extra.py
from unittest.mock import patch
from app.crud import create_user, read_users, update_user, delete_user


# 1) create_user uses parameterised SQL and returns True
@patch('app.crud.db_cursor')
def test_create_user_parameterised_and_success(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value

    result = create_user('Eve', 22)

    assert result is True

    # Check parameterised SQL: first positional arg is SQL, second is params
    sql, params = ctx.execute.call_args[0][0], ctx.execute.call_args[0][1]
    assert '?' in sql
    assert params == ('Eve', 22)


# 2) read_users maps DB tuples -> list of dicts
@patch('app.crud.db_cursor')
def test_read_users_maps_to_dicts(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    # Simulate pyodbc rows
    ctx.execute.return_value.fetchall.return_value = [
        (1, 'Alice', 29),
        (2, 'Bob', 31),
    ]

    users = read_users()

    assert users == [
        {'id': 1, 'name': 'Alice', 'age': 29},
        {'id': 2, 'name': 'Bob', 'age': 31},
    ]


# 3) update_user success path + parameterised SQL
@patch('app.crud.db_cursor')
def test_update_user_success_and_parameterised(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    # Simulate 1 affected row
    ctx.rowcount = 1

    result = update_user(1, name='Neo', age=30)

    assert result is True

    sql, params = ctx.execute.call_args[0][0], ctx.execute.call_args[0][1]
    assert 'UPDATE' in sql.upper()
    assert '?' in sql
    # Depending on your implementation this may be a list or tuple
    assert tuple(params) == ('Neo', 30, 1)


# 4) update_user with no fields provided -> returns False and does not run SQL
@patch('app.crud.db_cursor')
def test_update_user_no_fields_returns_false(mock_db_cursor):
    result = update_user(1)  # name=None, age=None
    assert result is False

    ctx = mock_db_cursor.return_value.__enter__.return_value
    ctx.execute.assert_not_called()


# 5) delete_user success path + parameterised SQL
@patch('app.crud.db_cursor')
def test_delete_user_success_and_parameterised(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    ctx.rowcount = 1

    result = delete_user(7)

    assert result is True

    sql, params = ctx.execute.call_args[0][0], ctx.execute.call_args[0][1]
    assert 'DELETE' in sql.upper()
    assert '?' in sql
    assert params == (7,)


# 6) delete_user not found -> returns False
@patch('app.crud.db_cursor')
def test_delete_user_not_found_returns_false(mock_db_cursor):
    ctx = mock_db_cursor.return_value.__enter__.return_value
    ctx.rowcount = 0

    assert delete_user(9999) is False