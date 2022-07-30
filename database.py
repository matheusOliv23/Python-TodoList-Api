from colorama import Cursor
from model import Todo

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoList
collection = database.todo


async def fetch_one_task(title):
  document = await collection.find_one({"title": title})
  return document


async def fetch_all_tasks():
  tasks = []
  cursor: collection.find({})
  async for document in cursor:
    tasks.append(Todo(**document))
  return tasks


async def create_task(task):
  document: task
  await collection.insert_one(document)
  return document


async def update_task(title, description):
  await collection.update_one({"title": title}, {"$set": {
      "description": description}})
  document = await collection.find_one({"title": title})
  return document


async def delete_task(title):
  await collection.delete_one({"title": title})
  return True
