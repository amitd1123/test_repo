```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    title: str
    description: str

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    try:
        return todos[todo_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    try:
        todos[todo_id] = todo
        return {"message": "Todo updated successfully", "todo": todo}
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    try:
        del todos[todo_id]
        return {"message": "Todo deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Todo not found")

@app.get("/todos")
def list_todos():
    return todos
```