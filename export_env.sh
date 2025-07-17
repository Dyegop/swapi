#!/bin/bash

# App Metadata
export APP_NAME="swapi"
export APP_HOST="127.0.0.1"
export APP_PORT=8000
export RELOAD_APP=true

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
