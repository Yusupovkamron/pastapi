from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")


@auth_router.get("/")
async def auth():
    return {
        "message": "this is auth page"
    }


@auth_router.get("/login")
async def login():
    return {
        "message": "this is login page"
    }


@auth_router.get("/register")
async def register():
    return {
        "message": "this is register page"
    }
