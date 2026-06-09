from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST API Assignment")


class Task(BaseModel):
    id: int
    title: str = Field(min_length=1)
    completed: bool = False


tasks: list[Task] = []


@app.get("/")
def root():
    return {"message": "Welcome to your FastAPI assignment API"}


@app.get("/tasks")
def list_tasks():
    return tasks


# TODO: Add POST /tasks
# TODO: Add GET /tasks/{task_id}
# TODO: Add PUT /tasks/{task_id}
# TODO: Add DELETE /tasks/{task_id}


def find_task(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
