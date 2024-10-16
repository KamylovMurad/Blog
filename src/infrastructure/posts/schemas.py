from datetime import datetime
from pydantic import BaseModel


class SchemaPost(BaseModel):
    id: int
    likes: int
    author: str
    theme: str
    body: str
    publication_date: datetime


class ShortSchemaPost(BaseModel):
    author: str
    theme: str
    body: str

