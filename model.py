from fastapi import APIRouter

model_router = APIRouter(prefix="/models")


@model_router.get("/")
async def model():
    return {
        "message": "model page"
    }


@model_router.get("/model")
async def model_1():
    return {
        "message": "model 1"
    }


@model_router.get("/model2")
async def model_2():
    return {
        "message": "model 2 page"
    }
