from fastapi import APIRouter

from services.demo_content import COURT_UPDATES

router = APIRouter()


@router.get("/")
async def get_court():
    return {"status": "operational", "updates": COURT_UPDATES}
