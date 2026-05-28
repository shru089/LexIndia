from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_citizen():
    return {"message": "Citizen endpoint"}
