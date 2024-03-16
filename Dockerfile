# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

RUN apt-get update
RUN apt-get install curl -y
RUN curl -sSL https://install.python-poetry.org | python3 -

# Prevents Python from writing pyc files.
# ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app/todo_app

# Copy the source code into the container.
COPY . .

ENV PATH="${PATH}:/root/.local/bin/"
RUN poetry install

FROM base as production
# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
# CMD poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
ENTRYPOINT [ "bash", "./my_entrypoint_prod.sh" ]

FROM base as development

# Expose the port that the application listens on.
EXPOSE 5000

# Run the application.
# CMD poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"
ENTRYPOINT [ "bash", "./my_entrypoint_dev.sh" ]

FROM base as test

ENTRYPOINT poetry run pytest

