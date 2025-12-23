import fastapi;
import uvicorn;
from fastapi import FastAPI
from .routers.users import router as users_router
app = FastAPI(title="Teaching Experience Demo")
app.include_router(users_router)
@app.get("/health")
def health_check():
    return {"status": "ok"}



