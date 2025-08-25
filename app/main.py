from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import os
from datetime import datetime

app = FastAPI(title="DevOps Demo App", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World from DevOps Pipeline!", "timestamp": datetime.now().isoformat()}

@app.get("/health")
async def health_check():
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0"
        }
    )

@app.get("/status")
async def status_check():
    return {"status": "running", "environment": os.getenv("ENVIRONMENT", "development")}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
