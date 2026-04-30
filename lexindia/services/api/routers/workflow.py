from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_workflow():
    return {"message": "Workflow endpoint"}
