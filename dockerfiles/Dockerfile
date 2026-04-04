FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY uv.lock pyproject.toml README.md ./

# Install dependencies
RUN uv sync --frozen --no-dev --no-install-project

# Copy the application code
COPY . .

# Sync the project
RUN uv sync --frozen --no-dev

# Install memu-py wheel if present (CI places .whl files in memu-wheel/ directory)
COPY memu-wheel/ /tmp/memu-wheel/
RUN if ls /tmp/memu-wheel/*.whl 1>/dev/null 2>&1; then \
      .venv/bin/pip install --force-reinstall --no-deps /tmp/memu-wheel/*.whl; \
    fi && rm -rf /tmp/memu-wheel

# Expose the port that FastAPI will run on
EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

CMD [ \
  "python", "-m", "gunicorn", \
  "--bind", "0.0.0.0:8000", \
  "--worker-class", "uvicorn.workers.UvicornWorker", \
  "app.main:app" \
]
