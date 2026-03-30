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

# Patch memu-py for Azure OpenAI compatibility (omit max_tokens=null)
# Copies fixed files from patches/ over the installed PyPI versions
COPY patches/azure-openai/ /tmp/memu-patches/
RUN MEMU_PATH=$(python -c "import memu; import os; print(os.path.dirname(memu.__file__))") && \
    cp /tmp/memu-patches/openai_sdk.py "$MEMU_PATH/llm/openai_sdk.py" && \
    cp /tmp/memu-patches/openai_backend.py "$MEMU_PATH/llm/backends/openai.py" && \
    rm -rf /tmp/memu-patches

# Expose the port that FastAPI will run on
EXPOSE 8000

ENV PATH="/app/.venv/bin:$PATH"

CMD [ \
  "python", "-m", "gunicorn", \
  "--bind", "0.0.0.0:8000", \
  "--worker-class", "uvicorn.workers.UvicornWorker", \
  "app.main:app" \
]
