from fastapi import FastAPI
from auth import auth_router
from model import model_router
app = FastAPI()
app.include_router(auth_router)
app.include_router(model_router)

@app.get("/test")
async def intro():
    return {
        "message": "this is landing page"
    }

@app.get("/test2")
async def tast2():
    return {
        "message": "this is test page "
    }