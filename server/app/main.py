import os
import debugpy

from dotenv import load_dotenv
from fastapi import FastAPI

from app.api.api import api_router
load_dotenv()

debugpy.listen(('0.0.0.0', int(os.getenv("FASTAPI_DEBUG_PORT"))))

app = FastAPI(
    root_path="/api"
)

app.include_router(api_router)


@app.get("")
async def root():
    return {"message": "Hello World"}
