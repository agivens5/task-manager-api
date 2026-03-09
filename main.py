from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def read_root():
    return {"message": "Task Manager API"}

# View all tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# Create a new task
@app.post("/tasks")
def create_task(task: str):
    new_task = {"task": task, "completed": False}
    tasks.append(new_task)
    return {"task_added": new_task}

# Mark a task as completed
@app.put("/tasks/{task_id}")
def complete_task(task_id: int):
    if task_id < len(tasks):
        tasks[task_id]["completed"] = True
        return {"updated_task": tasks[task_id]}
    return {"error": "Task not found"}

# Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        removed = tasks.pop(task_id)
        return {"deleted_task": removed}
    return {"error": "Task not found"}
