import motor.motor_asyncio
from app.models import Course
import json

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.kimo
course_collection = database.get_collection("courses")

async def fetch_all_courses():
    courses = []
    async for course in course_collection.find():
        courses.append(Course(**course))
    return courses

async def fetch_course(name: str):
    course = await course_collection.find_one({"name": name})
    if course:
        return Course(**course)

async def fetch_chapter(course_name: str, chapter_name: str):
    course = await course_collection.find_one({"name": course_name})
    if course:
        for chapter in course['chapters']:
            if chapter['name'] == chapter_name:
                return chapter

async def add_rating(course_name: str, chapter_name: str, rating: int):
    await course_collection.update_one(
        {"name": course_name, "chapters.name": chapter_name},
        {"$inc": {"chapters.$.rating": rating}}
    )
