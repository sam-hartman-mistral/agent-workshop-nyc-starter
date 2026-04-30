from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str = ""


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    created_at: str


class ErrorResponse(BaseModel):
    error: str
    detail: str
