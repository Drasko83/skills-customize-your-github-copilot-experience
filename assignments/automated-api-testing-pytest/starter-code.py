from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Automated API Testing with pytest")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks: list[Task] = []


def reset_tasks() -> None:
    tasks.clear()


def create_task(title: str) -> Task:
    cleaned = title.strip()
    if not cleaned:
        raise ValueError("Title must not be empty")

    task = Task(id=len(tasks) + 1, title=cleaned, completed=False)
    tasks.append(task)
    return task


def find_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


def complete_task(task_id: int) -> Task:
    task = find_task(task_id)
    task.completed = True
    return task


def delete_task(task_id: int) -> None:
    task = find_task(task_id)
    tasks.remove(task)


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task_endpoint(payload: TaskCreate):
    return create_task(payload.title)


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return find_task(task_id)


@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    delete_task(task_id)
    return {"message": "Task deleted"}
