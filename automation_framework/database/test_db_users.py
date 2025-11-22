import pytest
import os
from automation_framework.database.db_client import DBClient
from automation_framework.api.api_client import APIClient

@pytest.fixture
def db_client(worker_id):
    db_name = f"test_db_{worker_id}.sqlite"
    client = DBClient(db_name=db_name)
    client.connect()
    # Setup schema
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    client.execute_script(schema_path)
    # Clear table
    client.execute_query("DELETE FROM users")
    yield client
    client.close()
    # Cleanup
    # if os.path.exists(db_name):
    #     os.remove(db_name)

def test_insert_users(db_client):
    users = [
        (1, "Alice", "Active"),
        (2, "Bob", "Inactive"),
        (3, "Charlie", "Active")
    ]
    for user in users:
        db_client.execute_query("INSERT INTO users (id, name, status) VALUES (?, ?, ?)", user)
    
    rows = db_client.fetch_all("SELECT * FROM users")
    assert len(rows) == 3

def test_user_names_sorted(db_client):
    users = [
        (2, "Bob", "Inactive"),
        (1, "Alice", "Active"),
        (3, "Charlie", "Active")
    ]
    for user in users:
        db_client.execute_query("INSERT INTO users (id, name, status) VALUES (?, ?, ?)", user)
    
    rows = db_client.fetch_all("SELECT name FROM users ORDER BY name ASC")
    names = [row[0] for row in rows]
    assert names == ["Alice", "Bob", "Charlie"]

def test_api_to_db_integration(db_client):
    api = APIClient()
    response = api.get_users()
    api_users = response.json()
    
    for user in api_users:
        db_client.execute_query("INSERT OR IGNORE INTO users (id, name, status) VALUES (?, ?, ?)", (user['id'], user['name'], 'Active'))
    
    rows = db_client.fetch_all("SELECT * FROM users")
    assert len(rows) == len(api_users)
    
    # Verify ID uniqueness (SQLite PRIMARY KEY constraint handles this, but we can check count)
    ids = [row[0] for row in rows]
    assert len(ids) == len(set(ids))
