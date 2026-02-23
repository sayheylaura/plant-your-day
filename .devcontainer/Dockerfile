FROM mcr.microsoft.com/devcontainers/python:3.13

# Install uv (Python package manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /code
