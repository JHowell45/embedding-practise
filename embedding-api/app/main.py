import uvicorn
from fastapi import FastAPI

from app.routers import router

app = FastAPI(title="Embedding API")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
