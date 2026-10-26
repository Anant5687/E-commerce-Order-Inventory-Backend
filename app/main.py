from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def health_check():
    return {"status": 200, "details": "Health status 200"}
