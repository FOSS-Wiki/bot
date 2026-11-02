FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN useradd --create-home --shell /bin/bash app \
 && mkdir -p /app /opt/venv \
 && chown app:app /app /opt/venv

WORKDIR /app

ENV UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_LINK_MODE=copy \
    PATH="/opt/venv/bin:$PATH"

USER app

COPY --chown=app:app pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev --no-install-project

COPY --chown=app:app . .

CMD ["python", "bot.py"]
