
from typing import List, Dict, Any
from app.db import db_cursor


def create_user(name: str, age: int) -> bool:
    """Insert a new user. Returns True if an insert occurred."""
    sql = "INSERT INTO dbo.Users (Name, Age) VALUES (?, ?)"
    with db_cursor() as cur:
        cur.execute(sql, (name, age))
        return True


def read_users() -> List[Dict[str, Any]]:
    """Return all users as a list of dicts."""
    sql = "SELECT Id, Name, Age FROM dbo.Users ORDER BY Id"
    with db_cursor() as cur:
        rows = cur.execute(sql).fetchall()
        return [
            {"id": r[0], "name": r[1], "age": r[2]} for r in rows
        ]


def update_user(user_id: int, name: str = None, age: int = None) -> bool:
    """Update provided fields for a user. Returns True if a row was updated."""
    sets = []
    params = []
    if name is not None:
        sets.append("Name = ?")
        params.append(name)
    if age is not None:
        sets.append("Age = ?")
        params.append(age)
    if not sets:
        return False
    params.append(user_id)

    sql = f"UPDATE dbo.Users SET {', '.join(sets)} WHERE Id = ?"
    with db_cursor() as cur:
        cur.execute(sql, params)
        return cur.rowcount > 0


def delete_user(user_id: int) -> bool:
    """Delete a user by Id. Returns True if a row was deleted."""
    sql = "DELETE FROM dbo.Users WHERE Id = ?"
    with db_cursor() as cur:
        cur.execute(sql, (user_id,))
        return cur.rowcount > 0
