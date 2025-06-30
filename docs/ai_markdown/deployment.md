# Deployment & Configuration

## Overview
This document describes the deployment and configuration process for the Simple Model Manager project.

- Docker-based deployment
- Environment variable configuration
- Production and development setup

This file will be updated as deployment and configuration evolve.

## Dockerfile
- Multi-stage build using `python:3.9-slim` for both builder and production stages.
- Builder stage installs dependencies to a user-local directory.
- Production image copies only necessary files and dependencies.
- Environment variables for Flask and model configuration are set in the image.
- Placeholder for model download (customize as needed).
- Healthcheck added for `/health` endpoint.

## Environment-Specific Configuration
- Supports loading environment variables from a `.env` file using `python-dotenv`.
- See `.env.example` for all supported variables.

## CI/CD Pipeline
- Recommended: Use GitHub Actions for automated testing and deployment. 