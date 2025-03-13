FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

ENV UV_PYTHON_DOWNLOADS=0

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN uv sync --no-install-project --no-dev

COPY app .

RUN uv sync --frozen --no-dev

FROM python:3.12-slim-bookworm

COPY --from=builder --chown=app:app /app /app

ENV PATH="/app/.venv/bin:$PATH"

CMD ["fastapi", "run", "--host", "0.0.0.0"]