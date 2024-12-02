import uvicorn
from fastapi import FastAPI

from snowflake import *

app = FastAPI()
app.include_router(router=snowflake)


@app.get("/")
async def root():
    return {"metricore": "up"}


if __name__ == "__main__":
    uvicorn.run(app)
