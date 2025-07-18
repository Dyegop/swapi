FROM python:3.13.5-alpine AS builder

ENV PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

COPY app-requirements ./requirements
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements


FROM python:3.13.5-alpine

WORKDIR /app

COPY --from=builder /wheels /wheels
RUN pip install --upgrade pip && pip install --no-cache-dir --quiet /wheels/* && rm -r /wheels

COPY src/core src/core
COPY src/app src/app

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["sh", "-c", "uvicorn src.app.app:app --host $HOST --port $PORT"]
