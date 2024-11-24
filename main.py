from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"metricore": "up and running"}


if __name__ == "__main__":
    uvicorn.run(app)
