import uvicorn
from fastapi import FastAPI

from src.app.api.v1 import people_router, planets_router
from src.core import get_app_config

app = FastAPI(title="SWAPI", version="0.1.0")

app_config = get_app_config()

app.include_router(people_router, prefix="/people", tags=["people"])
app.include_router(planets_router, prefix="/planets", tags=["planets"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_config.app_host,
        port=app_config.app_port,
        reload=app_config.reload,
    )
