from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

## App objeto
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
    return 1


@app.get("/api/todo-{id}")
async def get_task_by_id(id):
  return 1


@app.post("/api/todo")
async def post_task(task):
  return 1


@app.put("/api/todo-{id}")
async def put_task(id, data):
  return 1


@app.delete("/api/todo-{id}")
async def delete_task(id):
  return 1
