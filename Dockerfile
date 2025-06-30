# syntax=docker/dockerfile:1

# Builder stage
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production image
FROM python:3.9-slim
WORKDIR /app

# Accept model config as build arguments (can be set via --build-arg or from .env)
ARG MODEL_TYPE=nllb-600m
ARG MODEL_PATH=/models/nllb-600m
ARG FLASK_ENV=production
ARG LOG_LEVEL=INFO

# Set environment variables in the image
ENV MODEL_TYPE=${MODEL_TYPE} \
    MODEL_PATH=${MODEL_PATH} \
    FLASK_ENV=${FLASK_ENV} \
    LOG_LEVEL=${LOG_LEVEL}

# Copy only necessary files
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
COPY . .

# Placeholder for model download (uncomment and customize as needed)
# RUN mkdir -p /models/nllb-600m && \
#     wget -O /models/nllb-600m/model.bin <MODEL_URL>

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["flask", "run", "--host=0.0.0.0"]
