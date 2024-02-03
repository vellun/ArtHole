from typing import Annotated
from fastapi import FastAPI, Path
import uvicorn
from pydantic import EmailStr, BaseModel

from api_v1 import router as router_v1
from core.config import settings

app = FastAPI()

app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000)

# source venv/Scripts/activate
# uvicorn main:app --reload --port 5000