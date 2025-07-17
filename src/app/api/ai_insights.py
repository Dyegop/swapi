from typing import Literal

from fastapi import APIRouter

from src.app.models import Insight
from src.app.services import generate_description
from src.core import Tags, get_resource_config

router = APIRouter()

resource_config = get_resource_config()


@router.get("/", response_model=Insight, tags=[Tags.AI_INSIGHTS])
async def simulate_ai_insight(resource_type: Literal["person", "planet"], name: str) -> Insight:
    """Mocks an AI-generated description for the given resource and name."""
    description = await generate_description(resource_type=resource_type, name=name)
    return Insight(name=name, description=description)
