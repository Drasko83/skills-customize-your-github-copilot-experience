from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from fastapi.testclient import TestClient
import pytest

_module_path = Path(__file__).with_name("starter-code.py")
_spec = spec_from_file_location("starter_code", _module_path)
starter_code = module_from_spec(_spec)
assert _spec and _spec.loader
_spec.loader.exec_module(starter_code)

app = starter_code.app
complete_task = starter_code.complete_task
create_task = starter_code.create_task
delete_task = starter_code.delete_task
reset_tasks = starter_code.reset_tasks

client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_state():
    reset_tasks()


def test_create_task_sets_default_completed_false():
    task = create_task("Read pytest docs")
    assert task.title == "Read pytest docs"
    assert task.completed is False


def test_create_task_rejects_empty_title():
    with pytest.raises(ValueError):
        create_task("   ")


def test_complete_task_marks_task_done():
    task = create_task("Write tests")
    updated = complete_task(task.id)
    assert updated.completed is True


def test_delete_task_removes_existing_task():
    task = create_task("Delete me")
    delete_task(task.id)
    assert client.get("/tasks").json() == []


def test_get_tasks_returns_list():
    create_task("Task A")
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_tasks_creates_task():
    response = client.post("/tasks", json={"title": "Practice API tests"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Practice API tests"


def test_get_task_by_id_success():
    response = client.post("/tasks", json={"title": "Lookup task"})
    task_id = response.json()["id"]

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == task_id


def test_get_task_by_id_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_delete_task_endpoint_success():
    response = client.post("/tasks", json={"title": "Delete endpoint task"})
    task_id = response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Task deleted"
