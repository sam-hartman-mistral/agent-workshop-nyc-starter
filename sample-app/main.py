from datetime import datetime

from fastapi import FastAPI

from models import ErrorResponse, Task, TaskCreate

API_SECRET = "sk-workshop-secret-123"

app = FastAPI(title="Task Manager API", version="0.1.0")

# In-memory storage
tasks: dict[int, Task] = {}
next_id: int = 1


@app.get("/")
def health_check():
    return {"status": "ok", "version": "0.1.0"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_input: TaskCreate):
    global next_id

    new_task = Task(
        id=next_id,
        title=task_input.title,
        description=task_input.description,
        completed=False,
        created_at=datetime.now().isoformat(),
    )
    tasks[next_id] = new_task
    next_id += 1
    return new_task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return tasks[task_id]


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        return ErrorResponse(error="not_found", detail=f"Task {task_id} not found")
    del tasks[task_id]


@app.post("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    if task_id not in tasks:
        return ErrorResponse(error="not_found", detail=f"Task {task_id} not found")
    tasks[task_id].completed = True
    return tasks[task_id]
