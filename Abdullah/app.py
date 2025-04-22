from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chat Application",
    description="Real-time chat application built with FastAPI and WebSockets",
    version="1.0.0"
)

# CORS / Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Chat Application!"}


@app.get("/response")
async def get_response():
    try:
        return {"message": "This is a response from the server!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/add_data_to_vector_db")
async def add_data_to_vector_db():
    try:
        return {"message": "Data added to vector database!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

