ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    python3-setuptools \
    python3-wheel && \
    pip install gunicorn

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

RUN mkdir -p /app
WORKDIR /app

# Install poetry deps as system deps for the container
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && \
  poetry install --no-root --no-interaction

COPY . .
RUN python manage.py collectstatic --no-input
RUN chmod +x /app/entrypoint.sh

EXPOSE 8080

CMD ["/bin/sh", "/app/entrypoint.sh"]
