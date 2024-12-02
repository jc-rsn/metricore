from fastapi import APIRouter

from snowflake.snowflake import *

snowflake = APIRouter(
    prefix="/snowflake",
    tags=["snowflake"]
)


@snowflake.get("/id")
async def snowflake_get_id():
    return {'snowflake_id': generate()}
