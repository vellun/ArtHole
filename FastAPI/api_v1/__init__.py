from fastapi import APIRouter

from .posts.views import router as posts_pouter

router = APIRouter()
router.include_router(router=posts_pouter, prefix="/posts")