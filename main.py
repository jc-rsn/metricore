from fastapi import FastAPI
import uvicorn

import snowflake.main as snowflake

app = FastAPI()


@app.get("/")
async def root():
    return {"metricore": "up"}


@app.get("/snowflake_id")
async def get_snowflake_id():
    return {"snowflake_id": snowflake.generate()}


if __name__ == "__main__":
    uvicorn.run(app)
