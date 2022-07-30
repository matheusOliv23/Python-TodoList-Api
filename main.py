from turtle import title
from urllib import response
from database import (create_task, remove_task,
                      fetch_all_tasks, fetch_one_task, update_task)
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import Todo

# App objeto
app = FastAPI()


origins = ['http://localhost:3000/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return ("Testando")


@app.get("/api/todo")
async def get_tasks():
    response = await fetch_all_tasks()
    return response


@app.get("/api/todo-{title}", response_model=Todo)
async def get_task_by_id(title):
    response = await fetch_one_task(title)
    if response:
        return response
    raise HTTPException(404, f"Não existe tarefa com o titulo {title}")


@app.post("/api/todo", response_model=Todo)
async def post_task(task: Todo):
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, 'Algo deu errado')


@app.put("/api/todo-{title}", response_model=Todo)
async def put_task(title: str, description: str):
    response = await update_task(title, description)
    if response:
        return response
    raise HTTPException(404, f"Não existe tarefa com o título {title}")


@app.delete("/api/todo-{title}")
async def delete_task(title):
    response = await remove_task(title)
    if response:
        return "Tarefa removida com sucesso"
    raise HTTPException(404, f"Não existe tarefa com o título {title}")
