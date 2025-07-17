import uvicorn
from fastapi import FastAPI

from src.app.api import ai_insights_router, people_router, planets_router
from src.core import Tags, get_app_config, get_resource_config

app = FastAPI(title="SWAPI", version="0.1.0")

app_config = get_app_config()
resource_config = get_resource_config()

app.include_router(people_router, prefix=app_config.people_path, tags=[Tags.PEOPLE])
app.include_router(planets_router, prefix=app_config.planets_path, tags=[Tags.PLANETS])
app.include_router(ai_insights_router, prefix=app_config.ai_insights_path, tags=[Tags.AI_INSIGHTS])


if __name__ == "__main__":
    uvicorn.run(
        "src.app.app:app",
        host=app_config.host,
        port=app_config.port,
        reload=app_config.reload,
    )
