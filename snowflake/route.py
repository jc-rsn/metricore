from fastapi import APIRouter

from snowflake.main import *

snowflake = APIRouter(
    prefix="/snowflake",
    tags=["snowflake"]
)


@snowflake.get("/id")
async def snowflake_get_id():
    return {'id': create_snowflake_id()}
