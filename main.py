from fastapi import FastAPI

app = FastAPI()

#The root path will be used as the health check endpoint
@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Service is online."}
