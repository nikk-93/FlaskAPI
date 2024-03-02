from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool


tasks = {}


@app.get("/tasks", response_model=List[Task])
def get_tasks() -> List[Task]:
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=Task)
def create_task(task: Task) -> Task:
    task.id = len(tasks) + 1
    tasks[task.id] = task
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task
    return task


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks.pop(task_id)
    return deleted_task
