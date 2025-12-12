from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/", summary="main fuck", tags=["too many fucks"])
async def root():
    return "fuck"

@app.get("/fuck")
async def fuck():
    return "too too many fucks"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)