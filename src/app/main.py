import uvicorn
from fastapi import FastAPI

from src.app.api.v1 import people_router, planets_router

app = FastAPI(title="SWAPI", version="0.1.0")

app.include_router(people_router, prefix="/people", tags=["people"])
app.include_router(planets_router, prefix="/planets", tags=["planets"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
