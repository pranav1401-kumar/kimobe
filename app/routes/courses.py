from fastapi import APIRouter, Query
from typing import List, Optional
from ..services.database import fetch_all_courses, fetch_course

router = APIRouter()

@router.get("/")
async def get_courses(sort_by: str = Query("alphabetical"), domain: Optional[str] = None):
    courses = await fetch_all_courses()
    if domain:
        courses = [course for course in courses if domain in course.domain]
    if sort_by == "alphabetical":
        courses.sort(key=lambda x: x.name)
    elif sort_by == "date":
        courses.sort(key=lambda x: x.date, reverse=True)
    return courses

@router.get("/{course_name}")
async def get_course_overview(course_name: str):
    course = await fetch_course(course_name)
    return course
