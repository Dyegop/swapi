import uvicorn
from fastapi import FastAPI

from src.app.api.v1 import people_router, planets_router
from src.core import get_app_config, get_resource_config

app = FastAPI(title="SWAPI", version="0.1.0")

app_config = get_app_config()
resource_config = get_resource_config()

app.include_router(people_router, prefix="/people", tags=[resource_config.people_resource])
app.include_router(planets_router, prefix="/planets", tags=[resource_config.planets_resource])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_config.host,
        port=app_config.port,
        reload=app_config.reload,
    )
