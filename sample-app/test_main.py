from fastapi.testclient import TestClient

from main import app, tasks

client = TestClient(app)


def setup_function():
    """Clear tasks before each test."""
    tasks.clear()


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Buy groceries", "description": "Milk, eggs, bread"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Buy groceries"
    assert data["completed"] is False
    assert "id" in data


def test_list_tasks():
    # Create two tasks first
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


# TODO: Add tests for delete, complete, and error cases
