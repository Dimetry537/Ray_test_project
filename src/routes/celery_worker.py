from fastapi import APIRouter
from src.tasks.tasks import copy_photo

router = APIRouter(
    prefix="/celery",
    tags=["Celery worker"]
)

@router.post("/copy-photo")
async def copy_photo_handler(src: str, dst: str):
    task = copy_photo.delay(src, dst)
    return {
        "message": "Copy started",
        "task_id": task.id
    }
