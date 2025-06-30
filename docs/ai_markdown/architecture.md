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

## Service Layer
- `app/services/model_service.py`: Contains `ModelService`, responsible for loading the language model and providing a `translate` method. This service is used by the translation route for all inference operations.
- `app/services/file_parser.py`: Provides the `FileParser` class for detecting, parsing, and extracting data from JSON/YAML files. Includes format detection, parsing, leaf node extraction, and validation utilities.
- `app/services/translation_service.py`: Provides the `TranslationService` class for prompt template management, batch translation, error handling, and result caching.

## API Endpoints
- `/translate` (POST): Accepts JSON with `text`, `source_lang`, and `target_lang`. Calls `ModelService.translate` and returns the translation result. Registered via a Flask blueprint in `app/routes/translate.py` and integrated in the app factory. 

## Language Code Management
- `app/utils/language_codes.py`: Provides a two-digit code to language name mapping, language code validation, and supported language enumeration utilities. Used by the `/languages` endpoint for supported language listing. 