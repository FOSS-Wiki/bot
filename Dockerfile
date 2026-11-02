FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN useradd --create-home --shell /bin/bash app

COPY pyproject.toml uv.lock* ./

RUN chown -R app:app /app

USER app

RUN uv sync --frozen --no-dev --no-install-project

COPY --chown=app:app . .

ENV PATH="/app/.venv/bin:$PATH"

CMD ["uv", "run", "python", "bot.py"]
