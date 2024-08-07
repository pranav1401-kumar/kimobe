from fastapi import APIRouter, HTTPException
from ..models import Rating
from ..services.database import add_rating

router = APIRouter()

@router.post("/")
async def rate_chapter(rating: Rating):
    if rating.rating not in [-1, 1]:
        raise HTTPException(status_code=400, detail="Rating must be either -1 or 1")
    await add_rating(rating.course_name, rating.chapter_name, rating.rating)
    return {"message": "Rating added successfully"}
