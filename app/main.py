from fastapi import FastAPI
from .routes import courses, chapters, ratings

app = FastAPI()

app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(chapters.router, prefix="/chapters", tags=["chapters"])
app.include_router(ratings.router, prefix="/ratings", tags=["ratings"])
