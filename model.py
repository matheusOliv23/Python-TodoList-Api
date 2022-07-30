from lib2to3.pytree import Base
from pydantic import BaseModel


class Todo(BaseModel):
  title: str
  description: str
