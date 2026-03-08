from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def read_root():
  return {"message": "Task Manager API"}

@app.get("/tasks")
def get_tasks():
  return tasks

@app.post("/tasks")
def create_task(task: str):
  tasks.append(task)
  return {"task_added": task}
