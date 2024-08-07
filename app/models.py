from pydantic import BaseModel, Field
from typing import List, Optional

class Chapter(BaseModel):
    name: str
    text: str

class Course(BaseModel):
    name: str
    date: int
    description: str
    domain: List[str]
    chapters: List[Chapter]

class Rating(BaseModel):
    course_name: str
    chapter_name: str
    rating: int
