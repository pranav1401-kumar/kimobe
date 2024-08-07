import asyncio
from app.services.database import create_courses

async def init():
    await create_courses()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
