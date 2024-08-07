from fastapi import APIRouter
from ..services.database import fetch_chapter

router = APIRouter()

@router.get("/{course_name}/{chapter_name}")
async def get_chapter(course_name: str, chapter_name: str):
    chapter = await fetch_chapter(course_name, chapter_name)
    return chapter
