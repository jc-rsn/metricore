from fastapi import APIRouter

settings = APIRouter(
    prefix="/settings",
    tags=["settings"],
)


@settings.put("/")
asy
