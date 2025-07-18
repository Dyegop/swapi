#!/bin/bash

# App Metadata
export NAME="swapi"
export HOST="0.0.0.0"
export PORT=8000
export RELOAD=true

# App Endpoints
export PEOPLE_PATH="/people"
export PLANETS_PATH="/planets"
export AI_INSIGHTS_PATH="/ai-insights"

# SWAPI Integration
export SWAPI_BASE_URL="https://swapi.info/api"
export PEOPLE_ENDPOINT="${SWAPI_BASE_URL}/people"
export PLANETS_ENDPOINT="${SWAPI_BASE_URL}/planets"
export DEFAULT_PAGE_SIZE=10

echo "Environment variables exported."
