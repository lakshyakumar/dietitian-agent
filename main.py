from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from router.dietitian import router as dietitian_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Mock project info
PROJECT_INFO = {
    "name": "Chat API",
    "version": "1.0.0",
    "description": "A FastAPI project for handling chat queries."
}


# Request model for /chat API
class ChatRequest(BaseModel):
    chat_id: str
    query: str

# Health API
@app.get("/health")
def health():
    return {"status": "healthy"}

# Info API
@app.get("/")
def info():
    return PROJECT_INFO

# Chat API
app.include_router(dietitian_router, prefix="/chat", tags=["dietitian"])

# Run the application (if running directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)