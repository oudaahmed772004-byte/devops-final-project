# =========================================================
# Dockerfile - Notes Info Server
# =========================================================
# Base image choice: python:3.12-slim
#   - Official, actively maintained image.
#   - "slim" variant is much smaller than the full python image
#     (no unnecessary build tools / docs), which keeps the final
#     image lean and reduces the attack surface.
#   - Debian-based, so it plays well with pip-installed wheels
#     without needing extra system libraries for this app.
#
# Best practices applied (2+ required):
#   1) Multi-stage build   -> dependencies are installed in a
#      throw-away "builder" stage; only the final runtime image
#      is kept, so build tools never ship in the final image.
#   2) Non-root user        -> the app runs as "appuser", not root.
#   3) Environment-variable configuration -> APP_MESSAGE / APP_PORT
#      change app behavior without touching the code.
#   4) HEALTHCHECK           -> Docker can automatically detect if
#      the web server stops responding.
# =========================================================

# ---------- Stage 1: builder ----------
FROM python:3.12-slim AS builder

WORKDIR /build

COPY app/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# ---------- Stage 2: final runtime image ----------
FROM python:3.12-slim

LABEL maintainer="your.email@example.com"
LABEL description="Notes Info Server - DevOps Final Project (Docker module)"

# Create a non-root user/group to run the application
RUN groupadd -r appgroup && useradd -r -g appgroup -m appuser

# Bring in the Python packages built in the builder stage
COPY --from=builder /root/.local /home/appuser/.local

WORKDIR /app

# Copy application source and sample data
COPY app/app.py .
COPY app/*.txt ./data/

# Make sure the appuser owns everything it needs
RUN chown -R appuser:appgroup /app /home/appuser/.local

# Environment-variable based configuration (with sensible defaults)
ENV APP_MESSAGE="Hello from Docker!" \
    APP_PORT=5000 \
    DATA_DIR=/app/data \
    PATH="/home/appuser/.local/bin:${PATH}"

USER appuser

EXPOSE 5000

# Docker will mark the container unhealthy if the /health endpoint
# stops responding correctly.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request,os; urllib.request.urlopen(f'http://127.0.0.1:{os.environ.get(\"APP_PORT\",5000)}/health').read()" || exit 1

CMD ["python", "app.py"]
