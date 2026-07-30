from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):

    isbn: str
    title: str
    author: str
    publisher: str
    pages: int
    url: str
    collected_at: str = datetime.now().isoformat()