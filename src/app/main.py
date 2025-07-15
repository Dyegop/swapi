import uvicorn
from fastapi import FastAPI

from src.app.api.v1 import people_router, planets_router
from src.core import get_config

app = FastAPI(title="SWAPI", version="0.1.0")

config = get_config()

app.include_router(people_router, prefix="/people", tags=["people"])
app.include_router(planets_router, prefix="/planets", tags=["planets"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=config.app_host,
        port=config.app_port,
        reload=config.reload,
    )
