"""
FastAPI backend for Learn React project.

This module provides example API routes for learning full-stack development
with React frontend and Python FastAPI backend.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

app = FastAPI(
    title="Learn React API",
    description="Backend API for Learn React learning project",
    version="0.1.0"
)

# Configure CORS for development and production
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "https://learn-webdev-nine.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint for API health check."""
    return {"message": "Learn React API is running!"}


@app.get("/api/hello")
async def hello(name: str = "World") -> Dict[str, str]:
    """
    Example endpoint demonstrating a simple web service.
    
    Args:
        name: Name to greet (default: "World")
        
    Returns:
        Greeting message
    """
    return {"message": f"Hello, {name}!"}


@app.get("/api/data")
async def get_data() -> Dict[str, Any]:
    """
    Example endpoint returning structured data.
    
    Returns:
        Sample data object
    """
    return {
        "title": "Sample Data",
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ],
        "timestamp": "2024-03-08T00:00:00Z"
    }


@app.post("/api/echo")
async def echo(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Example POST endpoint that echoes back the received data.
    
    Args:
        data: Any JSON data
        
    Returns:
        Same data back with a timestamp
    """
    return {
        "received": data,
        "message": "Data received successfully"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
