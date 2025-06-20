from pydantic import BaseModel


class CreateTaskRequest(BaseModel):
    description: str
    username: str


class CreateTaskResponse(BaseModel):
    id: int


class CompleteTaskRequest(BaseModel):
    id: int
    username: str


class CompleteTasksRequest(BaseModel):
    username: str
