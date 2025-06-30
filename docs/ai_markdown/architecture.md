# Project Architecture

## Overview
This document describes the structure and design of the Simple Model Manager project.

- Flask-based translation service
- Modular, swappable language model architecture
- JSON/YAML file processing and translation

## Directory Structure
```
app/
  __init__.py
  models/
  services/
  routes/
  utils/
config/
tests/
```

## Key Components
- **app/**: Main application code
- **config/**: Configuration files
- **tests/**: Unit and integration tests

This file will be updated as the architecture evolves. 

## Flask Application Factory
The app uses a factory pattern in `app/__init__.py`:
- `create_app()` initializes and returns a Flask app instance.
- Registers a `/health` endpoint for health checks.

## Configuration Management
- `config/settings.py` provides a `Config` class that loads environment variables for model selection and app settings.

## Application Entry Point
- `run.py` creates the app and runs it on port 5000 (container default). 