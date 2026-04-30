from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_docs():
    return {"message": "Documents endpoint"}
